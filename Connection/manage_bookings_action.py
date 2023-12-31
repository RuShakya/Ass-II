import mysql.connector
from mysql.connector import Error
from conn import conn

def manage_bookings_action():
    try:
        
        db_connection = conn()
        cursor = db_connection.cursor()
        
        # get the combined data details from the database
        query = "SELECT * FROM tbl_all_bookings"
        cursor.execute(query)
        all_bookings_details = cursor.fetchall()
        
        # close data base connection
        cursor.close()
        db_connection.close()
        
        return all_bookings_details
    
    except Error as e:
        print(f"Error: {e}")
        return None
    
    