from tkinter import messagebox
import mysql.connector
from conn import conn

def update_action(up_customer_id, up_booking_id, up_pick_up_address, up_drop_off_address, up_date, up_time ):
    # Get the database connection
    db_connection = conn()
    
    if db_connection:
        try:
            cursor = db_connection.cursor()
            query = "UPDATE tbl_booking SET Pick_Up_Address=%s, Drop_Off_Address=%s, Pick_Up_Date=%s, Pick_Up_Time=%s WHERE customer_id=%s AND booking_id=%s"
            cursor.execute(query, (up_pick_up_address, up_drop_off_address, up_date, up_time, up_customer_id, up_booking_id))
            
            # Commit the changes and close the connection
            db_connection.commit()
            db_connection.close()

            # Check if any rows were affected
            if cursor.rowcount > 0:
                messagebox.showinfo("Trip Updated", "Booked Trip Updated Successfully.")
                print(up_customer_id)
                return True, up_customer_id
            else:
                messagebox.showinfo("Trip Not Updated", "Booked Trip can't be updated.")
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor and connection
            cursor.close()
            db_connection.close()

    return False
         
        