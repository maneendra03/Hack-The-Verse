import mysql.connector

try:
    # Establish connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nani*2005",
        database="pharmacy_db"
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # SQL statement to create 'users' table with 'email' as primary key
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        full_name VARCHAR(100) NOT NULL,
        email VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL
    )
    """

    # Execute table creation SQL
    mycursor.execute(create_table_sql)

    # Get user input for email to check if it exists
    email_to_check = input("Enter email to check if it exists: ")

    # SQL statement to select user details by email
    select_user_sql = "SELECT * FROM users WHERE email = %s"
    mycursor.execute(select_user_sql, (email_to_check,))
    existing_user = mycursor.fetchone()

    if existing_user:
        print("User found with email:", email_to_check)
        print("User Details:", existing_user)
    else:
        print("User not found with email:", email_to_check)
        print("Inserting new user...")

        # Get user input for attributes
        full_name = input("Enter full name: ")
        email = email_to_check
        password = input("Enter password: ")

        # SQL statement to insert data into the 'users' table
        insert_user_sql = "INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)"
        val = (full_name, email, password)

        # Execute the SQL query with the values
        mycursor.execute(insert_user_sql, val)

        # Commit changes to the database
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

except mysql.connector.Error as error:
    print("Error interacting with MySQL:", error)
    if 'email' in str(error):
        print("Failed to insert. Email already exists as a primary key.")

finally:
    # Close the database connection
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")
