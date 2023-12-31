import mysql.connector
from mysql.connector import Error
from conn import conn

def get_drivers_data():
    try:
        db_connection = conn()
        if db_connection is None:
            print("Error: Unable to establish a database connection.")
            return None

        cursor = db_connection.cursor()

        query = """
        SELECT
            d.Driver_ID,
            d.Name,
            d.Address,
            d.Phone_Number,
            d.Email,
            d.Username,
            d.Licence_Number,
            t.Taxi_Plate_Number,
            t.Taxi_Status
        FROM
            tbl_driver d
        LEFT JOIN
            tbl_taxi t ON d.Driver_ID = t.Driver_ID"""

        cursor.execute(query)
        drivers_data = cursor.fetchall()

        # Close database connection
        cursor.close()
        db_connection.close()

        return drivers_data

    except Error as e:
        print(f"Error: {e}")
        return None
