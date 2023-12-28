
from tkinter import messagebox
import mysql.connector
from conn import conn

def book_now_action(pick_address, drop_address, pick_date, pick_time, agree):
    # Get the database connection
    db_connection = conn()
    
    if db_connection:
        try:
            cursor = db_connection.cursor()
            query = "INSERT INTO tbl_booking (Pick_Up_Address, Drop_Off_Address, Pick_Up_Date, Pick_Up_Time, Terms_And_Conditions, Booking_Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (
                pick_address,    
                drop_address,
                pick_date,
                pick_time,
                "Accepted",
                "Pending",
                
            )
            cursor.execute(query, data)
            db_connection.commit()
        
            # Check if any rows were affected
            if cursor.rowcount > 0:
                messagebox.showinfo("Trip Booked", "Trip Booked Successfully.")
                return True
            else:
                messagebox.showinfo("No Trip Booked", "Trip can't be booked")
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor and connection
            cursor.close()
            db_connection.close()

    return False
