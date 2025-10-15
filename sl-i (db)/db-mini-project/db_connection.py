import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # your MySQL username
        password="root",  # your MySQL password
        database="student_enrollment_db"
    )
    return conn
