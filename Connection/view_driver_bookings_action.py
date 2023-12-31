import mysql.connector
from mysql.connector import Error
from conn import conn

def view_driver_bookings_action(driver_id):
    try:
        db_connection = conn()
        cursor = db_connection.cursor()

        # get the bookings details for a specific driver from the database
        query = "SELECT * FROM tbl_all_bookings WHERE Driver_ID = %s"
        cursor.execute(query, (driver_id,))
        driver_bookings = cursor.fetchall()

        # close database connection
        cursor.close()
        db_connection.close()

        return driver_bookings

    except Error as e:
        print(f"Error: {e}")
        return None