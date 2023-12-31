import tkinter as tk
from tkinter import ttk, messagebox  
import re 
from PIL import Image, ImageTk
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Connection')
import conn
import add_driver_action
import delete_driver_action
import global_all
import customer_details_action
import view_drivers_action
import manage_bookings_action


class Admin_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Admin Dashboard Page")

        # database connection details
        from conn import conn
        self.db_connection = conn()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.resizable(False, False)
        self.images()
        self.headings()
        self.frames()
        self.buttons_indicators()
        self.hide_indicators()
        self.indicate(self.home_indicate, self.home_page)    # Automatically open the home page
    
    def execute_query(self, query, data, fetchone=False):
        try:
            db_connection = conn()
            if db_connection is None:
                print("Error: Unable to establish a database connection.")
                return None

            cursor = db_connection.cursor()
            cursor.execute(query, data)

            if fetchone:
                result = cursor.fetchone()
            else:
                result = None

            db_connection.commit()

            cursor.close()
            db_connection.close()

            return result

        except Exception as e:
            print(f"Error: {e}")
            return None

    def headings(self):
        self.lbl_title1 = tk.Label(self, width=8, bg="#104E8B", anchor="w")
        self.lbl_title1.place(x=-20, y=0, height=90)

        self.lbl_title2 = tk.Label(self, text="Admin Dashboard", width=50, font=("Times New Roman", 40, "bold"), fg="yellow", bg="#104E8B", anchor="w")
        self.lbl_title2.place(x=40, y=0, height=90)

        self.lbl_welcome = tk.Label(self, text="Welcome", width=10, font=("Candara", 38, "bold"), fg="white", bg="#104E8B", anchor="e")
        self.lbl_welcome.place(x=1190, y=0, height=90)

        self.lbl_side = tk.Label(self, width=50, bg="#104E8B", anchor="w")
        self.lbl_side.place(x=-1, y=90, height=900)
        
    def images(self):
        self.image_1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_101.jpg")
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
    
    def frames(self):
        self.main_frame = tk.Frame(self, highlightbackground="black", highlightthickness=0)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1268, height=790)
        self.main_frame.place(x=271, y=90)
        

    def hide_indicators(self):
        self.home_indicate.config(bg="#104E8B")
        self.manage_drivers_indicate.config(bg="#104E8B")
        self.view_drivers_indicate.config(bg="#104E8B")
        self.manage_bookings_indicate.config(bg="#104E8B")
        self.view_customers_details_indicate.config(bg="#104E8B")

    def destroy_pages(self):
        for frame in self.main_frame.winfo_children():
          frame.destroy()
            
    def indicate(self, lb, page_func):    
        self.hide_indicators()
        lb.config(bg="white")
        self.destroy_pages()
        page_func(self.main_frame)

    def buttons_indicators(self):
        # Home Button
        self.btn_home = tk.Button(self, text="Home", width=15, font=("Candara", 23, "bold"), fg="white", bg="#104E8B", bd=0, command=lambda: self.indicate(self.home_indicate, self.home_page))
        self.btn_home.place(x=-2, y=170, height=40)

        # Home_Indicator
        self.home_indicate = tk.Label(self, text=" ", bg="black")
        self.home_indicate.place(x=0, y=170, width=10, height=40)

        # Manage Drivers Button
        self.btn_manage_drivers = tk.Button(self, text="Manage Drivers", width=15, font=("Candara", 23, "bold"), fg="white", bg="#104E8B", bd=0, command=lambda: self.indicate(self.manage_drivers_indicate, self.manage_drivers_page))
        self.btn_manage_drivers.place(x=-2, y=290, height=40)

        # Manage_Drivers_Indicator
        self.manage_drivers_indicate = tk.Label(self, text=" ", bg="black")
        self.manage_drivers_indicate.place(x=0, y=290, width=10, height=40)

        # View Drivers Button
        self.btn_view_drivers = tk.Button(self, text="View Drivers", width=15, font=("Candara", 23, "bold"), fg="white", bg="#104E8B", bd=0, command=lambda: self.indicate(self.view_drivers_indicate, self.view_drivers_page))
        self.btn_view_drivers.place(x=-2, y=440, height=40)

        # View_Drivers_Indicator
        self.view_drivers_indicate = tk.Label(self, text=" ", bg="black")
        self.view_drivers_indicate.place(x=0, y=440, width=10, height=40)

        # Manage Bookings Button
        self.btn_manage_bookings = tk.Button(self, text="Manage Bookings", width=15, font=("Candara", 23, "bold"), fg="white", bg="#104E8B", bd=0, anchor="e", command=lambda: self.indicate(self.manage_bookings_indicate, self.manage_bookings_page))
        self.btn_manage_bookings.place(x=-2, y=590, height=40)

        # Manage_Bookings_Indicator
        self.manage_bookings_indicate = tk.Label(self, text=" ", bg="black")
        self.manage_bookings_indicate.place(x=0, y=590, width=10, height=40)
        
        # View Customers Details Button 
        self.btn_view_customers_details = tk.Button(self, text="  Customers Details", width=15, font=("Candara", 23, "bold"), fg="white", bg="#104E8B", bd=0, command=lambda: self.indicate(self.view_customers_details_indicate, self.customers_details_page))
        self.btn_view_customers_details.place(x=-1, y=740, height=40)
        
        #View_Customers_Details_Indicator
        self.view_customers_details_indicate = tk.Label(self, text=" ", bg="black")
        self.view_customers_details_indicate.place(x=0, y=740, width=10, height=40)
        
    # show password
    def toggle_password(self):
        if self.show_password_var_1.get() == 1:
            self.txt_password.config( show="")
        else:
            self.txt_password.config(show="*")
            
    def on_treeview_select(self, event):
        # Get the selected item in the Treeview
        item = event.widget.selection()[0]
        values = event.widget.item(item, "values")

        # Extract customer_id and booking_id from the selected row
        customer_id, booking_id = values[0], values[3] 

        # Set the values in the corresponding entry fields
        self.txt_customer_id.delete(0, tk.END)
        self.txt_customer_id.insert(0, customer_id)

        self.txt_booking_id.delete(0, tk.END)
        self.txt_booking_id.insert(0, booking_id)

    def go_to_everyone_login(self):
        # Ask for confirmation
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        # If user confirms, proceed with the logout
        if confirm:
            self.destroy()
            from everyone_login import Everyone_login
            everyone_login_page = Everyone_login(self)
            everyone_login_page.mainloop()
        else:
            # Stay in the same page
            pass
    

    def home_page(self, frame):  
        self.alabel = tk.Label(self.main_frame, image=self.photo_1)
        self.alabel.place(x=-10, y=-550)
                     
        self.lbl_1 = tk.Label(self.main_frame, width=30, text="Ensuring A Seemless Experience", font=("Candara", 30, "bold"), fg="black", bg="light gray", bd=1)
        self.lbl_1.place(x=600, y=90, height=65)
        
        self.lbl_2 = tk.Label(self.main_frame, width=25, text=" Control Without Complexity", font=("Candara", 30, "bold"), fg="black", bg="light gray")
        self.lbl_2.place(x=710, y=190, height=65)
        
        self.btn_logout = tk.Button(self.main_frame, text="Log Out", width=13, font=("Candara", 23, "bold"), fg="black", bg="light gray", command=self.go_to_everyone_login)
        self.btn_logout.place(x=990, y=650, height=50)
        
    def manage_drivers_page(self, frame):    
        self.lbl_1 = tk.Label(self.main_frame, width=20, text="Manage Drivers", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        self.lbl_1.place(x=830, y=60, height=65)
        
        self.lbl_frame = tk.Frame(self.main_frame, width=10000, bg="light gray")
        self.lbl_frame.place(x=-10, y=185, height=900)
        
        self.lbl_driver_name = tk.Label(self.main_frame, text="Driver's Name: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_driver_name.place(x=50, y=250)
        self.txt_driver_name = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_name.place(x=250, y=250, height=35)
        
        self.lbl_driver_address = tk.Label(self.main_frame, text="Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_driver_address.place(x=700, y=250)
        self.txt_driver_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_address.place(x=900, y=250, height=35)
        
        self.lbl_driver_phone = tk.Label(self.main_frame, text="Phone Number: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_driver_phone.place(x=50, y=350)
        self.txt_driver_phone = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_phone.place(x=250, y=350, height=35)
        
        self.lbl_driver_email = tk.Label(self.main_frame, text="Email Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_driver_email.place(x=700, y=350)
        self.txt_driver_email = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_email.place(x=900, y=350, height=35)
        
        self.lbl_username = tk.Label(self.main_frame, text="Username: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_username.place(x=50, y=450)
        self.txt_username = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_username.place(x=250, y=450, height=35)
        
        self.lbl_password = tk.Label(self.main_frame, text="Password: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_password.place(x=700, y=450)
        self.txt_password = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1, show="*")
        self.txt_password.place(x=900, y=450, height=35)
                
        self.show_password_var_1 = tk.IntVar(self.main_frame)
        self.chk_show_password_1 = tk.Checkbutton(self.main_frame, width=1, variable=self.show_password_var_1, command=self.toggle_password)
        self.chk_show_password_1.place(x=1177, y=451, height=33)
        
        self.lbl_licence_number = tk.Label(self.main_frame, text="Licence Number: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_licence_number.place(x=50, y=550)
        self.txt_licence_number = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_licence_number.place(x=250, y=550, height=35)
        
        self.lbl_taxi_plate_number = tk.Label(self.main_frame, text="Taxi Plate Number: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_taxi_plate_number.place(x=700, y=550)
        self.txt_taxi_plate_number = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_taxi_plate_number.place(x=900, y=550, height=35)
        
        self.btn_add_driver = tk.Button(self.main_frame, text="Add Driver", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0, command=self.add_driver_button_action)
        self.btn_add_driver.place(x=330, y=640, height=50)
        
        self.btn_delete_driver = tk.Button(self.main_frame, text="Delete Driver", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0, command=self.delete_driver_action)
        self.btn_delete_driver.place(x=980, y=640, height=50)
        

    def view_drivers_page(self, frame):
        lbl_1 = tk.Label(self.main_frame, width=20, text="View Drivers", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=60, height=65)
        
        # Create Treeview widget for displaying drivers
        tree = ttk.Treeview(self.main_frame, columns=("Driver_ID", "Name", "Address", "Phone_Number", "Email", "Username", "Licence_Number", "Taxi_Plate_Number", "Taxi_Status"))
        tree.heading("#0", text="Index", anchor=tk.W)
        tree.column("#0", width=50)
        tree.heading("Driver_ID", text="Driver ID", anchor=tk.W)
        tree.column("Driver_ID", width=80)
        tree.heading("Name", text="Name", anchor=tk.W)
        tree.column("Name", width=120)
        tree.heading("Address", text="Address", anchor=tk.W)
        tree.column("Address", width=120)
        tree.heading("Phone_Number", text="Phone Number", anchor=tk.W)
        tree.column("Phone_Number", width=150)
        tree.heading("Email", text="Email", anchor=tk.W)
        tree.column("Email", width=150)
        tree.heading("Username", text="Username", anchor=tk.W)
        tree.column("Username", width=120)
        tree.heading("Licence_Number", text="Licence Number", anchor=tk.W)
        tree.column("Licence_Number", width=150)
        tree.heading("Taxi_Plate_Number", text="Taxi Plate Number", anchor=tk.W)
        tree.column("Taxi_Plate_Number", width=150)
        tree.heading("Taxi_Status", text="Taxi_Status", anchor=tk.W)
        tree.column("Taxi_Status", width=139)

        # Fetch and display drivers data from the database
        drivers_data = view_drivers_action.get_drivers_data()
        if drivers_data:
            for index, driver in enumerate(drivers_data):
                tree.insert("", index, text=str(index + 1), values=driver)

            tree.place(x=15, y=180, height=510)

        else:
            messagebox.showwarning("No Data", "No drivers data found.")

        # Add scrollbar to the treeview
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=tree.yview)
        scrollbar.place(x=177 + 1050, y=182, height=505)

        tree.configure(yscrollcommand=scrollbar.set)


    def manage_bookings_page(self, frame): 
        lbl_1 = tk.Label(self.main_frame, width=20, text="Manage Bookings", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=60, height=65)
        
        # Create Treeview widget for displaying bookings
        tree = ttk.Treeview(self.main_frame, columns=("Customer_ID", "Customer_Name", "Customer_Phone_Number", "Booking_ID", "Pick_Up_Address", "Drop_Off_Address", "Pick_Up_Date", "Pick_Up_Time", "Booking_Status", "Driver_ID", "Driver_Name", "Driver_Phone_Number", "Taxi_Plate_Number", "Taxi_Status"))
        tree.heading("#0", text="Index", anchor=tk.W)
        tree.column("#0", width=50)
        tree.heading("Customer_ID", text="Customer ID", anchor=tk.W)
        tree.column("Customer_ID", width=80)
        tree.heading("Customer_Name", text="Customer Name", anchor=tk.W)
        tree.column("Customer_Name", width=150)
        tree.heading("Customer_Phone_Number", text="Customer Phone Number", anchor=tk.W)
        tree.column("Customer_Phone_Number", width=160)
        tree.heading("Booking_ID", text="Booking ID", anchor=tk.W)
        tree.column("Booking_ID", width=80)
        tree.heading("Pick_Up_Address", text="Pick Up Address", anchor=tk.W)
        tree.column("Pick_Up_Address", width=120)
        tree.heading("Drop_Off_Address", text="Drop Off Address", anchor=tk.W)
        tree.column("Drop_Off_Address", width=120)
        tree.heading("Pick_Up_Date", text="Pick Up Date", anchor=tk.W)
        tree.column("Pick_Up_Date", width=120)
        tree.heading("Pick_Up_Time", text="Pick Up Time", anchor=tk.W)
        tree.column("Pick_Up_Time", width=120)
        tree.heading("Booking_Status", text="Booking Status", anchor=tk.W)
        tree.column("Booking_Status", width=120)
        tree.heading("Driver_ID", text="Driver ID", anchor=tk.W)
        tree.column("Driver_ID", width=80)
        tree.heading("Driver_Name", text="Driver Name", anchor=tk.W)
        tree.column("Driver_Name", width=150)
        tree.heading("Driver_Phone_Number", text="Driver Phone Number", anchor=tk.W)
        tree.column("Driver_Phone_Number", width=150)
        tree.heading("Taxi_Plate_Number", text="Taxi Plate Number", anchor=tk.W)
        tree.column("Taxi_Plate_Number", width=150)
        tree.heading("Taxi_Status", text="Taxi Status", anchor=tk.W)
        tree.column("Taxi_Status", width=150)
        
        # Fetch and display bookings data from the database
        bookings_data = manage_bookings_action.manage_bookings_action()
        if bookings_data:
            for index, booking in enumerate(bookings_data):
                tree.insert("", index, text=str(index + 1), values=booking)

            # Add a binding to the Treeview selection event
            tree.bind("<ButtonRelease-1>", self.on_treeview_select)
            
            tree.place(x=15, y=180, height=230, width=1230)
            
             # Add scrollbar to the treeview (vertical scrollbar)
            y_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=tree.yview)
            y_scrollbar.place(x=178 + 1050, y=182, height=228)

            # Add scrollbar to the treeview (horizontal scrollbar)
            x_scrollbar = ttk.Scrollbar(self.main_frame, orient="horizontal", command=tree.xview)
            x_scrollbar.place(x=15, y=400, width=1230)

            # Configure treeview to use scrollbars
            tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
   
        else:
            messagebox.showwarning("No Data", "No bookings data found.")

        self.lbl_customer_id = tk.Label(self.main_frame, text="Customer ID: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_customer_id.place(x=50, y=450)
        self.txt_customer_id = tk.Entry(self.main_frame, width=15, font=("Candara", 15), bd=1)
        self.txt_customer_id.place(x=220, y=450, height=35)
        
        self.lbl_booking_id = tk.Label(self.main_frame, text="Booking ID: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_booking_id.place(x=495, y=450)
        self.txt_booking_id = tk.Entry(self.main_frame, width=15, font=("Candara", 15), bd=1)
        self.txt_booking_id.place(x=645, y=450, height=35)
        
        self.lbl_driver_id = tk.Label(self.main_frame, text="Driver ID: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_driver_id.place(x=910, y=450)
        self.txt_driver_id = tk.Entry(self.main_frame, width=15, font=("Candara", 15), bd=1)
        self.txt_driver_id.place(x=1040, y=450, height=35)
        
        self.lbl_driver_name = tk.Label(self.main_frame, text="Driver Name: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_driver_name.place(x=50, y=550)
        self.txt_driver_name = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_name.place(x=220, y=550, height=35)
        
        self.lbl_driver_phone_number = tk.Label(self.main_frame, text="Driver Phone: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_driver_phone_number.place(x=730, y=550)
        self.txt_driver_phone_number = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_phone_number.place(x=900, y=550, height=35)
        
        self.lbl_taxi_plate_number = tk.Label(self.main_frame, text="Taxi Number: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_taxi_plate_number.place(x=50, y=650)
        self.txt_taxi_plate_number = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_taxi_plate_number.place(x=220, y=650, height=35)
        
        self.btn_accept_booking = tk.Button(self.main_frame, text="Accept Booking", width=15, font=("Candara", 20, "bold"), fg="white", bg="brown", bd=0, command=self.accept_booking_action)
        self.btn_accept_booking.place(x=980, y=650, height=50)        
        
       
        
    def customers_details_page(self, frame): 
        lbl_1 = tk.Label(self.main_frame, width=20, text="Customers Details", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=60, height=65)

        # Create Treeview widget for displaying customer details
        tree = ttk.Treeview(self.main_frame, columns=("Customer_ID", "Name", "Address", "Phone_Number", "Email", "Username", "Payment_Method"))
        tree.heading("#0", text="Index", anchor=tk.W)
        tree.column("#0", width=50)
        tree.heading("Customer_ID", text="Customer ID", anchor=tk.W)
        tree.column("Customer_ID", width=80)
        tree.heading("Name", text="Name", anchor=tk.W)
        tree.column("Name", width=190)
        tree.heading("Address", text="Address", anchor=tk.W)
        tree.column("Address", width=200)
        tree.heading("Phone_Number", text="Phone Number", anchor=tk.W)
        tree.column("Phone_Number", width=120)
        tree.heading("Email", text="Email", anchor=tk.W)
        tree.column("Email", width=200)
        tree.heading("Username", text="Username", anchor=tk.W)
        tree.column("Username", width=190)
        tree.heading("Payment_Method", text="Payment Method", anchor=tk.W)
        tree.column("Payment_Method", width=200)

        # Fetch and display customer details from the database
        customer_details = customer_details_action.get_customer_details()
        if customer_details:
            for index, customer in enumerate(customer_details):
                tree.insert("", index, text=str(index + 1), values=customer)

            tree.place(x=15, y=180, height=510)

        else:
            messagebox.showwarning("No Data", "No customer details found.")

        # Add scrollbar to the treeview
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=tree.yview)
        scrollbar.place(x=177 + 1050, y=182, height=505)

        tree.configure(yscrollcommand=scrollbar.set)

    
    
    #####################============================== Action for btn_add_driver ==========================================================================
    def add_driver_button_action(self):
        # Validation for name
        name = self.txt_driver_name.get()
        if not name.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Name.")
            return
        
        # Validation for address
        address = self.txt_driver_address.get()
        if not address.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Address.")
            return

        # Validation for phone 
        phone = self.txt_driver_phone.get()
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Invalid Phone Number")
            return
        
        # Validation for email
        email = self.txt_driver_email.get()
        email_pattern = re.compile(r'^[a-zA-Z0-9]+(_[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$')
        if not email_pattern.match(email):
            messagebox.showerror("Error", "Invalid Email Address. Please enter a valid email.")
            return
        
        # Validation for username
        username = self.txt_username.get()
        if not username.replace(" ", "").isalnum() or len(username) > 30:
            messagebox.showerror("Error", "Please use appropriate username.")
            return

        # Validation for password
        password = self.txt_password.get()
        if not password.replace(" ", "").isalnum() or len(password) > 30:
            messagebox.showerror("Error", "Please use appropriate password.")   
            return
        
        #================================= Set global variables=====================================================================================================================================
        global_all.global_driver_username = username
        global_all.global_driver_password = password
        #=============================================================================================================================================================================================================================
       
        # Validation for licence number
        licence_number = self.txt_licence_number.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', licence_number):
            messagebox.showerror("Error", "Invalid Licence Number. Please enter a valid licence number.")
            return
        
        # Validation for taxi plate number
        taxi_plate_number = self.txt_taxi_plate_number.get()
        if not taxi_plate_number.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Name.")
            return
        
        #========================================================DB=============================================================================================================================================================================================================================
        from add_driver_action import add_driver_action
        driver_id = global_all.global_driver_id
        result = add_driver_action(name, address, phone, email, username, password, licence_number, taxi_plate_number)
        
        if result:
            self.clear_entry_fields()  
            # Store driver_id in global variable
            global_all.global_driver_id = driver_id
      
     
     
    def delete_driver_action(self):
        name = self.txt_driver_name.get()
        if not name.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Name.")
            return
        
        username = self.txt_username.get()
        if not username.replace(" ", "").isalnum() or len(username) > 30:
            messagebox.showerror("Error", "Please use appropriate username.")
            return
        
        password = self.txt_password.get()
        if not password.replace(" ", "").isalnum() or len(password) > 30:
            messagebox.showerror("Error", "Please use appropriate password.")   
            return
        
        licence_number = self.txt_licence_number.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', licence_number):
            messagebox.showerror("Error", "Invalid Licence Number. Please enter a valid licence number.")
            return
        
        taxi_plate_number = self.txt_taxi_plate_number.get()
        if not taxi_plate_number.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Taxi Plate Number.")
            return
         
        from delete_driver_action import delete_driver_action
        result = delete_driver_action(name, username, password, licence_number, taxi_plate_number)
        
        if result:
            self.clear_entry_fields() 
    
    
    def accept_booking_action(self):
        customer_id = self.txt_customer_id.get()
        booking_id = self.txt_booking_id.get()
        driver_id = self.txt_driver_id.get()
        
        # Validate input data
        if not customer_id.isdigit() or not booking_id.isdigit() or not driver_id.isdigit():
            messagebox.showerror("Error", "Invalid input. Please enter valid ID.")
            return
        
        driver_name = self.txt_driver_name.get()
        if not driver_name.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Name.")
            return
        
        driver_phone_number = self.txt_driver_phone_number.get()
        if not driver_phone_number.isdigit() or len(driver_phone_number) != 10:
            messagebox.showerror("Error", "Invalid Phone Number")
            return
        
        taxi_plate_number = self.txt_taxi_plate_number.get()
        if not taxi_plate_number:
            messagebox.showerror("Error", "Invalid Taxi Plate Number.")
            return False
    
        from accept_booking_action import accept_booking_action
        result = accept_booking_action(
            customer_id,
            booking_id,
            'Accepted',
            driver_id,
            driver_name,
            driver_phone_number,
            taxi_plate_number,
            'Booked'
        )
        
            
    # Clear All Entries
    def clear_entry_fields(self):
        # Clear all entry fields
        self.txt_driver_name.delete(0, tk.END)
        self.txt_driver_address.delete(0, tk.END)
        self.txt_driver_phone.delete(0, tk.END)
        self.txt_driver_email.delete(0, tk.END)
        self.txt_username.delete(0, tk.END)
        self.txt_password.delete(0, tk.END)
        self.txt_licence_number.delete(0, tk.END)
        self.txt_taxi_plate_number.delete(0, tk.END)
        
    
        

if __name__ == '__main__':
    gui = Admin_dashboard()
    gui.mainloop()
    
    
    
    
    
    
    
    
    
    
    