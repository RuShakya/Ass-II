from tkinter import messagebox
import mysql.connector
from conn import conn

def cancel_action(cancel_customer_id, cancel_booking_id):
    # Get the database connection
    db_connection = conn()
    if db_connection:
        try:
            cursor = db_connection.cursor()

            query = "DELETE FROM tbl_booking WHERE Booking_ID=%s AND Customer_ID=%s"
            
            # Execute the query with the provided values
            cursor.execute(query, (cancel_customer_id, cancel_booking_id))
            
            # Commit the changes to the database
            db_connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Booking Deleted", "Booking Canceled successfully.")
                return True
            else:
                messagebox.showinfo("No Booking Deleted", "No matching booking found for cancelation.")
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor and connection
            cursor.close()
            db_connection.close()

    return False

