from tkinter import Tk
from tkinter import messagebox
import mysql.connector
from conn import conn

def login_action(username, password):
    try:
        
        # get datbase connection 
        db_connection = conn()
        
        if db_connection:
        
            # create a cursor
            cursor = db_connection.cursor() 
            
            # customer login
            cursor.execute("SELECT * FROM tbl_customer WHERE username=%s AND password=%s", (username, password))
            customer_data = cursor.fetchone()
                    
            # Admin login
            cursor.execute("SELECT * FROM tbl_admin WHERE username=%s AND password=%s", (username, password))
            admin_data = cursor.fetchone()  

            # Close the database connection
            db_connection.close()
            
            
            # MESSAGE BOX
            if customer_data:
                messagebox.showinfo("Welcome Customer", "Customer Login Successful.")
                return "customer"
            elif admin_data:
                messagebox.showinfo("Welcome Admin", "Admin Login Successful.")
                return "admin"
            else:
                messagebox.showerror("Error", "Invalid Username or Password!")
                return None   
        

    except mysql.connector.Error as err:
        custom_error_message = "Nooooooooooo errorrrrrrrrrrrrr"
        messagebox.showerror("Error", f"{custom_error_message}\nMySQL Error: {err}")
        # Log the error or print for debugging purposes
        print(f"{custom_error_message}\nMySQL Error: {err}")

    return None
  