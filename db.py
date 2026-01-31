import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",               # change if needed
            password="aakrisht",   # change if needed
            database="ERP"          # your DB name
        )
        return connection
    except Error as e:
        print("❌ Database connection failed:", e)
        return None
