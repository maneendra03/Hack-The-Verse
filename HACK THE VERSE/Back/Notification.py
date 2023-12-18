import mysql.connector
from datetime import datetime, timedelta
import ssl
import smtplib
from email.message import EmailMessage

import schedule

# Database connection parameters
db_host = 'localhost'
db_user = 'root'
db_password = 'Nani*2005'
db_name = 'pharmacy'

# Establish database connection
def check_and_send_emails():
    try:
        conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()
        today_date = datetime.now().date()
        one_month_later = today_date + timedelta(days=30)

        # Fetch drugs expiring this month from the database
        values = "SELECT medicine_name, expiry_date FROM medicines WHERE expiry_date BETWEEN %s AND %s"
        cursor.execute(values, (today_date, one_month_later))

        expired_drugs = cursor.fetchall()

        # Close database connection
        cursor.close()
        print(expired_drugs)
        conn.close()

        # Prepare email content
        email_sender = 'adepuvaatsavasribhargav@gmail.com'
        email_password = 'tbja yqnx azyd xvma'
        email_receiver = '22h51a1250@cmrcet.ac.in'
        

        subject = 'List of drugs that are going to expire this month'
        body = "Please find the list of drugs that are going to expire this month:\n"
        for drug in expired_drugs:
            body += f"- {drug[0]}\n"

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        # Send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        print("Email sent successfully!")
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

# Schedule the job to run every day at a specific time (adjust this as needed)
schedule.every().day.at("20:55").do(check_and_send_emails)

while True:
    schedule.run_pending()