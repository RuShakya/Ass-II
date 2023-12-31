from tkinter import messagebox
import mysql.connector
from conn import conn

def trip_completed_action(customer_id, booking_id, driver_id, booking_status, taxi_status):
    
    db_connection = conn()
    if db_connection:
        try:
            cursor = db_connection.cursor()
            
            # Update into tbl_all_bookings
            update_all_bookings_query = "UPDATE tbl_all_bookings SET booking_status=%s, taxi_status=%s WHERE booking_id=%s"
            cursor.execute(update_all_bookings_query, (booking_status, taxi_status, booking_id))

            
            db_connection.commit()

            if cursor.rowcount > 0:
                # If the update on tbl_all_bookings is successful, proceed with other queries
                # Update tbl_booking
                update_booking_query = "UPDATE tbl_booking SET booking_status=%s WHERE booking_id = %s"
                cursor.execute(update_booking_query, (booking_status, booking_id))

                # Update tbl_taxi
                update_taxi_query = "UPDATE tbl_taxi SET taxi_status=%s WHERE driver_id = %s"
                cursor.execute(update_taxi_query, (taxi_status, driver_id))

                db_connection.commit()

                if cursor.rowcount > 0:
                    return True
                else:
                    return False
            else:
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor and connection
            cursor.close()
            db_connection.close()

    return False
