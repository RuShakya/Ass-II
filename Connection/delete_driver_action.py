from tkinter import messagebox
import mysql.connector
from conn import conn

def delete_driver_action(name, username, password, licence_number, taxi_plate_number):
    # Get the database connection
    db_connection = conn()

    if db_connection:
        cursor = None
        try:
            # Obtain the cursor
            cursor = db_connection.cursor()

            # First query to delete from tbl_driver
            query_1 = "DELETE FROM tbl_driver WHERE name=%s AND username=%s AND password=%s AND licence_number=%s"
            cursor.execute(query_1, (name, username, password, licence_number))

            # Second query to delete from tbl_taxi
            query_2 = "DELETE FROM tbl_taxi WHERE Taxi_Plate_Number=%s"
            cursor.execute(query_2, (taxi_plate_number,))

            # Commit the changes to the database
            db_connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Driver Deleted", "Driver deleted successfully.")
                return True
            else:
                messagebox.showinfo("No Driver Found", "No matching driver found for deletion.")
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            db_connection.close()

    return False
