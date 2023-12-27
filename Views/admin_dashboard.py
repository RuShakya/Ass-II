import tkinter as tk
from tkinter import messagebox  
import re 
from PIL import Image, ImageTk
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Connection')
import conn
import add_driver_action
import delete_driver_action

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
            self.txt_password.config(show="")
        else:
            self.txt_password.config(show="*")

        if self.show_password_var_2.get() == 1:
            self.txt_confirmpw.config(show="")
        else:
            self.txt_confirmpw.config(show="*")    

    def home_page(self, frame):   
        self.alabel = tk.Label(self.main_frame, image=self.photo_1)
        self.alabel.place(x=-10, y=-550)
                     
        self.lbl_1 = tk.Label(self.main_frame, width=30, text="Ensuring A Seemless Experience", font=("Candara", 30, "bold"), fg="black", bg="light gray", bd=1)
        self.lbl_1.place(x=600, y=510, height=65)
        
        self.lbl_2 = tk.Label(self.main_frame, width=25, text=" Control Without Complexity", font=("Candara", 30, "bold"), fg="black", bg="light gray")
        self.lbl_2.place(x=710, y=610, height=65)
        

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
        
        self.show_password_var_1 = tk.IntVar()
        self.chk_show_password_1 = tk.Checkbutton(self, width=1, variable=self.show_password_var_1, command=self.toggle_password)
        self.chk_show_password_1.place(x=1448, y=541, height=34)
        
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
        lbl_1.place(x=844, y=90, height=65)


    def manage_bookings_page(self, frame): 
        lbl_1 = tk.Label(self.main_frame, width=20, text="Manage Bookings", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=90, height=65)
        
    
    def customers_details_page(self, frame): 
        lbl_1 = tk.Label(self.main_frame, width=20, text="Customers Details", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=90, height=65)
        
    
    
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
        
        # Validation for licence number
        licence_number = self.txt_licence_number.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', licence_number):
            messagebox.showerror("Error", "Invalid Licence Number. Please enter a valid licence number.")
            return
        
        # Validation for taxi plate number
        taxi_plate_number = self.txt_taxi_plate_number.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', taxi_plate_number):
            messagebox.showerror("Error", "Invalid Taxi Plate Number.")
            return
        
        # DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        from add_driver_action import add_driver_action
        result = add_driver_action(name, address, phone, email, username, password, licence_number, taxi_plate_number)
        
        if result:
            self.clear_entry_fields()  
     
     
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
        if not re.match(r'^[a-zA-Z0-9/-]+$', taxi_plate_number):
            messagebox.showerror("Error", "Invalid Taxi Plate Number.")
            return
         
        from delete_driver_action import delete_driver_action
        result = delete_driver_action(name, username, password, licence_number, taxi_plate_number)
        
        if result:
            self.clear_entry_fields() 
            
    
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
    
    
    
    
    
    
    
    
    
    
    