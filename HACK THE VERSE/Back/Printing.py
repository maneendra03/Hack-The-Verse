import mysql.connector
from datetime import datetime, timedelta

try:
    # Establish connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nani*2005",  # Replace with your MySQL password
        database="pharmacy"
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()
    # Calculate today's date and the date one month from now
    today_date = datetime.now().date()
    one_month_later = today_date + timedelta(days=30)

    # SQL statement to select drugs that will expire within the next month
    select_drugs_sql = "SELECT medicine_name, expiry_date FROM medicines WHERE expiry_date BETWEEN %s AND %s"
    mycursor.execute(select_drugs_sql, (today_date, one_month_later))

    # Fetch all the drugs that will expire within the next month
    expiring_drugs = mycursor.fetchall()

    if expiring_drugs:
        print("Drugs that will expire within the next month:")
        for drug in expiring_drugs:
            print(f"Medicine Name: {drug[0]}, Expiry Date: {drug[1]}")
    else:
        print("No drugs are going to expire within the next month.")

except mysql.connector.Error as error:
    print("Error interacting with MySQL:", error)

finally:
    # Close the cursor and database connection
    if 'mycursor' in locals() and mycursor is not None:
        mycursor.close()
    if 'mydb' in locals() and mydb is not None and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")
