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

    # Get user input for attributes
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    # SQL statement to insert data into the 'users' table
    sql = "INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)"

    # Values to be inserted
    val = (full_name, email, password)

    # Execute the SQL query with the values
    mycursor.execute(sql, val)

    # Commit changes to the database
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

except mysql.connector.Error as error:
    print("Error inserting data into MySQL table:", error)

finally:
    # Close the database connection
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")
