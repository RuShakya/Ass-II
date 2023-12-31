from tkinter import messagebox
import mysql.connector
from conn import conn
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Views')
import global_all

def add_driver_action(name, address, phone, email, username, password, licence_number, taxi_plate_number):
    # Get the database connection
    db_connection = conn()

    if db_connection:
        try:
            cursor = db_connection.cursor()   
            
            query_1 = "INSERT INTO tbl_driver (Name, Address, Phone_Number, Email, Username, Password, Licence_Number, Admin_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data_1 = (
                name,
                address,
                phone,
                email,
                username,
                password,
                licence_number,
                1
            )
            cursor.execute(query_1, data_1)
            db_connection.commit()
            
            
            # Get the last inserted driver_id
            cursor.execute("SELECT LAST_INSERT_ID()")
            driver_id = cursor.fetchone()[0]
            
            
            query_2 = "INSERT INTO tbl_taxi (Taxi_Plate_Number, Taxi_Status, Driver_ID) VALUES (%s, %s, %s)"
            data_2 = (
                taxi_plate_number,
                "Available",
                driver_id
            )
            cursor.execute(query_2, data_2)
            db_connection.commit()

             # Update global variable with the retrieved driver_id
            global_all.global_driver_id = driver_id
            
            # Check if any rows were affected
            if cursor.rowcount > 0:
                messagebox.showinfo("Driver Added", "Driver Added Successfully.")
                return True
            else:
                messagebox.showinfo("No Driver Added", "Driver can't be added.")
                return False

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            # Close the cursor and connection
            cursor.close()
            db_connection.close()

    return False

