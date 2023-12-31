from tkinter import messagebox
import mysql.connector
from conn import conn

def register_action(name, address, phone, email, username, password, confirm_password, payment_method):
    # Get the database connection
    db_connection = conn()

    if db_connection:
        try:
            cursor = db_connection.cursor()
            query = "INSERT INTO tbl_customer (Name, Address, Phone_Number, Email, Username, Password, Confirm_Password, Payment_Method) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (
                name,
                address,
                phone,
                email,
                username,
                password,
                confirm_password,
                payment_method
            )
            cursor.execute(query, data)
            db_connection.commit()
            
            # Retrieve auto-incremented customer_id
            customer_id = cursor.lastrowid

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
            print("Error:", err)

        finally:
            db_connection.close()

        messagebox.showinfo("Registered", "Customer Registered Successfully.")
        return True, customer_id

    return False, None
