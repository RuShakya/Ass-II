import mysql.connector
from mysql.connector import Error
from conn import conn

def get_customer_details():
    try:
        
        db_connection = conn()
        cursor = db_connection.cursor()
        
        # get the customer details from the database
        query = "SELECT Customer_ID, Name, Address, Phone_Number, Email, Username, Payment_METHOD FROM tbl_customer"
        cursor.execute(query)
        customer_details = cursor.fetchall()
        
        # close data base connection
        cursor.close()
        db_connection.close()
        
        return customer_details
    
    except Error as e:
        print(f"Error: {e}")
        return None
    
    
        
        