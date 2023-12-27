from tkinter import messagebox
import mysql.connector
from conn import conn

def add_driver_action(name, address, phone, email, username, password, licence_number, taxi_plate_number):
    # Get the database connection
    db_connection = conn()

    if db_connection:
        try:
            cursor = db_connection.cursor()
            query = "INSERT INTO tbl_driver (Name, Address, Phone_Number, Email, Username, Password, Licence_Number, Taxi_Plate_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (
                name,
                address,
                phone,
                email,
                username,
                password,
                licence_number,
                taxi_plate_number
            )
            cursor.execute(query, data)
            db_connection.commit()

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

