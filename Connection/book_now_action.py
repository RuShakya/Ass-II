from tkinter import messagebox
import mysql.connector
from conn import conn
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Views')
import global_all

def book_now_action(pick_address, drop_address, pick_date, pick_time, agree, customer_id):
    # Get the database connection
    db_connection = conn()
    
    if db_connection:
        try:
            cursor = db_connection.cursor()
            
            # Retrieve customer_name based on customer_id
            customer_name_query = "SELECT name, phone_number FROM tbl_customer WHERE customer_id = %s"
            cursor.execute(customer_name_query, (customer_id,))
            customer_name_result = cursor.fetchone()
            
            if customer_name_result:
                customer_name = customer_name_result[0]
                customer_phone_number = customer_name_result[1]
            else:
                messagebox.showerror("Error", "Customer not found.")
                return False
            
            # Insert data into tbl_booking
            booking_query = "INSERT INTO tbl_booking (Pick_Up_Address, Drop_Off_Address, Pick_Up_Date, Pick_Up_Time, Terms_And_Conditions, Booking_Status, Customer_ID, Admin_ID, Driver_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            booking_data = (
                pick_address,    
                drop_address,
                pick_date,
                pick_time,
                "Accepted",
                "Pending",
                customer_id,
                0,
                0
            )
            cursor.execute(booking_query, booking_data)
            db_connection.commit()
        
            # Check if any rows were affected
            if cursor.rowcount > 0:
                # Fetch the last inserted booking_id
                cursor.execute("SELECT LAST_INSERT_ID()")
                booking_id_result = cursor.fetchone()
                if booking_id_result:
                    booking_id = booking_id_result[0]
                    # Insert data into tbl_combined_data
                    combined_query = """
                        INSERT INTO tbl_all_bookings
                        (customer_id, Customer_Name, Customer_Phone_Number, booking_id, pick_up_address, drop_off_address, pick_up_date, pick_up_time, booking_status, driver_id, driver_name, driver_phone_number, taxi_plate_number, taxi_status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    combined_data = (
                        customer_id,
                        customer_name,
                        customer_phone_number,
                        booking_id,
                        pick_address,
                        drop_address,
                        pick_date,
                        pick_time,
                        "Pending",
                        0,  # Default driver_id
                        "Pending",  # Default driver_name
                        0,  # Default driver_phone_number
                        0,  # Default taxi_plate_number
                        "Pending"
                    )
                    cursor.execute(combined_query, combined_data)
                    db_connection.commit()
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
