import mysql.connector

try:
    # Establish connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nani*2005",  # Replace with your password
        database="pharmacy"
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # Get user input for medicine details
    medicine_name = input("Enter medicine name: ")
    batch_no = input("Enter batch number: ")
    manufacturing_date = input("Enter manufacturing date (YYYY-MM-DD): ")
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    quantity = int(input("Enter quantity: "))

    # SQL statement to insert data into the 'medicines' table
    insert_medicine_sql = """
    INSERT INTO medicines 
    (medicine_name, batch_no, manufacturing_date, expiry_date, quantity) 
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Values to be inserted
    val = (medicine_name, batch_no, manufacturing_date, expiry_date, quantity)

    # Execute the SQL query with the values
    mycursor.execute(insert_medicine_sql, val)

    # Commit changes to the database
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

except mysql.connector.Error as error:
    print("Error interacting with MySQL:", error)

finally:
    # Close the database connection
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")
