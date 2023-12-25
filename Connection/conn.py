
import mysql.connector

def conn():
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxi_booking_system"
        )
        return connection
    
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None