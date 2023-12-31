from tkinter import Tk, messagebox
import mysql.connector
from conn import conn
import sys
import global_all

def login_action(username, password):
    try:
        # Get database connection 
        db_connection = conn()
        
        if db_connection:
            try:
                # Create a cursor
                cursor = db_connection.cursor() 
            
                # Customer login
                cursor.execute("SELECT * FROM tbl_customer WHERE username=%s AND password=%s", (username, password))
                customer_data = cursor.fetchone()
                    
                # Admin login
                cursor.execute("SELECT * FROM tbl_admin WHERE username=%s AND password=%s", (username, password))
                admin_data = cursor.fetchone()  

                # Driver Login
                cursor.execute("SELECT * FROM tbl_driver WHERE username=%s AND password=%s", (username, password))
                driver_data = cursor.fetchone() 
                
                # Close the database connection
                cursor.close()

                # MESSAGE BOX
                if customer_data:
                    customer_id = customer_data[0]  # Assuming customer_id is the first column in tbl_customer
                    global_all.global_customer_id = customer_id  # Set global_customer_id
                    messagebox.showinfo("Welcome Customer", "Customer Login Successful.")
                    return "customer", customer_id
                elif admin_data:
                    messagebox.showinfo("Welcome Admin", "Admin Login Successful.")
                    return "admin", None
                elif driver_data:
                    driver_id = driver_data[0]  # Assuming driver_id is the first column in tbl_driver
                    global_all.global_driver_id = driver_id  # Set global_driver_id
                    messagebox.showinfo("Welcome Driver", "Driver Login Successful.")
                    return "driver", driver_id
                else:
                    return None, None
            except mysql.connector.Error as err:
                # Handle database errors
                raise
            finally:
                # Ensure the database connection is closed
                db_connection.close()

    except Exception as e:
        # Handle other exceptions
        custom_error_message = "Damn Error"
        messagebox.showerror("Error", f"{custom_error_message}\nError: {e}")
        
        # Log the error for debugging purposes
        print(f"{custom_error_message}\nError: {e}")

    return None, None
