from tkinter import messagebox
import mysql.connector
from conn import conn

def delete_driver_action(name, username, password, licence_number, taxi_plate_number):
    # Get the database connection
    db_connection = conn()

    if db_connection:
        try:
            cursor = db_connection.cursor()

            # Use %s as placeholders for values
            query = "DELETE FROM tbl_driver WHERE name=%s AND username=%s AND password=%s AND licence_number=%s AND taxi_plate_number=%s"
            
            # Execute the query with the provided values
            cursor.execute(query, (name, username, password, licence_number, taxi_plate_number))

            # Commit the changes to the database
            db_connection.commit()

            # Check if any rows were affected
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
            cursor.close()
            db_connection.close()

    return False
