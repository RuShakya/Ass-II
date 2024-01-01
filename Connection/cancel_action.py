from tkinter import messagebox
import mysql.connector
from conn import conn

def cancel_action(cancel_customer_id, cancel_booking_id):
    # Get the database connection
    db_connection = conn()
    if db_connection:
        try:
            cursor = db_connection.cursor()

            # Use placeholders in the query to avoid SQL injection
            # Execute the first query to delete from tbl_booking
            query_booking = "DELETE FROM tbl_booking WHERE Booking_ID=%s AND Customer_ID=%s"
            cursor.execute(query_booking, (cancel_booking_id, cancel_customer_id))

            # Execute the second query to delete from tbl_all_bookings
            query_all_bookings = "DELETE FROM tbl_all_bookings WHERE Booking_ID=%s AND Customer_ID=%s"
            cursor.execute(query_all_bookings, (cancel_booking_id, cancel_customer_id))

            # Commit the changes
            db_connection.commit()

            # Check if any rows were affected
            if cursor.rowcount > 0:
                messagebox.showinfo("Trip Cancelled", "Booking Cancelled Successfully.")
                return True, cancel_customer_id
            else:
                messagebox.showerror("Trip Not Cancelled", "Booked Trip can't be cancelled.")
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor (if it exists) and connection
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            db_connection.close()

    return False
