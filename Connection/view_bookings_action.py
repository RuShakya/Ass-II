import mysql.connector
from mysql.connector import Error
from conn import conn

def view_bookings_action(customer_id):
    try:
        db_connection = conn()
        cursor = db_connection.cursor()

        # get the bookings details for a specific customer from the database
        query = "SELECT * FROM tbl_all_bookings WHERE Customer_ID = %s"
        cursor.execute(query, (customer_id,))
        customer_bookings = cursor.fetchall()

        # close database connection
        cursor.close()
        db_connection.close()

        return customer_bookings

    except Error as e:
        print(f"Error: {e}")
        return None
