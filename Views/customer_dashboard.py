import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from tkinter import messagebox 
import re 
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Connection')
import conn
import book_now_action
import update_action
import cancel_action
import view_bookings_action
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Views')
import global_all



class Customer_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Customer Dashboard Page")

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

    def images(self):
        self.image_1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_11.jpg")
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
        
        self.image_2 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_12.png")
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        
        self.image_3 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_13.jpg")
        self.photo_3 = ImageTk.PhotoImage(self.image_3)

    def headings(self):
        self.lbl_title1 = tk.Label(self, width=8, bg="black", anchor="w")
        self.lbl_title1.place(x=-20, y=0, height=90)

        self.lbl_title2 = tk.Label(self, text="Customer Dashboard", width=50, font=("Times New Roman", 40, "bold"), fg="yellow", bg="black", anchor="w")
        self.lbl_title2.place(x=40, y=0, height=90)

        self.lbl_welcome = tk.Label(self, text="Welcome", width=10, font=("Candara", 38, "bold"), fg="white", bg="black", anchor="e")
        self.lbl_welcome.place(x=1190, y=0, height=90)

        self.lbl_side = tk.Label(self, width=38, bg="black", anchor="w")
        self.lbl_side.place(x=-2, y=90, height=900)

    def frames(self):
        self.main_frame = tk.Frame(self, highlightbackground="black", highlightthickness=0)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1268, height=790)
        self.main_frame.place(x=271, y=90)
        

    def hide_indicators(self):
        self.home_indicate.config(bg="black")
        self.book_indicate.config(bg="black")
        self.view_indicate.config(bg="black")
        self.update_cancel_indicate.config(bg="black")

    def destroy_pages(self):
        for frame in self.main_frame.winfo_children():
          frame.destroy()
            
    def indicate(self, lb, page_func):    
        self.hide_indicators()
        lb.config(bg="yellow")
        self.destroy_pages()
        page_func(self.main_frame)

    def buttons_indicators(self):
        # Home Button
        self.btn_home = tk.Button(self, text="Home", width=15, font=("Candara", 23, "bold"), fg="white", bg="black", bd=0, command=lambda: self.indicate(self.home_indicate, self.home_page))
        self.btn_home.place(x=-2, y=190, height=40)

        # Home_Indicator
        self.home_indicate = tk.Label(self, text=" ", bg="black")
        self.home_indicate.place(x=0, y=190, width=10, height=40)

        # Book Button
        self.btn_book = tk.Button(self, text="Book A Trip", width=15, font=("Candara", 23, "bold"), fg="white", bg="black", bd=0, command=lambda: self.indicate(self.book_indicate, self.book_page))
        self.btn_book.place(x=-2, y=340, height=40)

        # Book_Indicator
        self.book_indicate = tk.Label(self, text=" ", bg="black")
        self.book_indicate.place(x=0, y=340, width=10, height=40)

        # View Button
        self.btn_view = tk.Button(self, text="View Bookings", width=15, font=("Candara", 23, "bold"), fg="white", bg="black", bd=0, command=lambda: self.indicate(self.view_indicate, self.view_page))
        self.btn_view.place(x=-2, y=490, height=40)

        # View_Indicator
        self.view_indicate = tk.Label(self, text=" ", bg="black")
        self.view_indicate.place(x=0, y=490, width=10, height=40)

        # Update_Cancel Button
        self.btn_update_cancel = tk.Button(self, text="Update/ Cancel", width=15, font=("Candara", 23, "bold"), fg="white", bg="black", bd=0, command=lambda: self.indicate(self.update_cancel_indicate, self.update_cancel_page))
        self.btn_update_cancel.place(x=-2, y=640, height=40)

        # Update_Cancel_Indicator
        self.update_cancel_indicate = tk.Label(self, text=" ", bg="black")
        self.update_cancel_indicate.place(x=0, y=640, width=10, height=40)

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
        self.alabel.place(x=-1, y=-500)
        
        self.lbl_1 = tk.Label(self.main_frame, width=20, text="Tap, Book, Roll", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        self.lbl_1.place(x=844, y=90, height=65)
        
        self.lbl_2 = tk.Label(self.main_frame, width=25, text=" Your Cozy Ride Awaits!", font=("Candara", 30, "bold"), fg="white", bg="brown")
        self.lbl_2.place(x=710, y=190, height=65)
        
        self.btn_logout = tk.Button(self.main_frame, text="Log Out", width=13, font=("Candara", 23, "bold"), fg="black", bg="yellow", command=self.go_to_everyone_login)
        self.btn_logout.place(x=990, y=650, height=50)
        

    def book_page(self, frame):    
        self.blabel = tk.Label(self.main_frame, image=self.photo_2)
        self.blabel.place(x=-330, y=40)
        
        self.lbl_frame = tk.Frame(self.main_frame, width=10000, bg="light gray")
        self.lbl_frame.place(x=-10, y=290, height=900)
        
        self.lbl_pick_address = tk.Label(self.main_frame, text="Pick Up Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_address.place(x=50, y=350)
        self.txt_pick_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_pick_address.place(x=250, y=350, height=35)
        
        
        self.lbl_drop_address = tk.Label(self.main_frame, text="Drop Off Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_drop_address.place(x=700, y=350)
        self.txt_drop_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_drop_address.place(x=900, y=350, height=35)
        
        self.lbl_pick_date = tk.Label(self.main_frame, text="Pick Up Date: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_date.place(x=50, y=450)
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        self.cal = DateEntry(self.main_frame, width=41, background='darkblue', foreground='white', borderwidth=2, year=today.year, month=today.month, day=today.day, font=("Candara", 10), mindate=today)
        self.cal.place(x=250, y=450, height=35)
        
        self.lbl_pick_time = tk.Label(self.main_frame, text="Pick Up Time: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_time.place(x=700, y=450)
        time_var = tk.StringVar()
        self.time_picker = ttk.Combobox(self.main_frame, width=22, textvariable=time_var, values=['12:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '08:00 AM', '9:00 AM', '10:00 AM', '11:00 AM','12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '04:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM'], font=("Candara", 17), state='readonly')
        self.time_picker.place(x=900, y=450, height=35)
        self.time_picker.set('08:00 AM')
        
        self.checkbox_var = tk.BooleanVar()
        self.chk_agree = tk.Checkbutton(self.main_frame, text="I agree that my submitted data is being collected and stored.", variable=self.checkbox_var, font=("Candara", 14), fg="black", bg="light gray")
        self.chk_agree.place(x=380, y=550)
        
        self.btn_book_now = tk.Button(self.main_frame, text="Book Now!", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0, command=self.book_now_action)
        self.btn_book_now.place(x=520, y=600, height=50)


    def view_page(self, frame):
        
        customer_id = global_all.global_customer_id  # Fetch the customer ID from the global variable
        #bookings = Connection.manage_bookings_action(customer_id)  # Assuming you have a function to fetch customer bookings

        self.lbl_1 = tk.Label(self.main_frame, width=33, text="View Your Bookings", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        self.lbl_1.place(x=590, y=50, height=85)

        # Display bookings in a tkinter widget (e.g., Treeview)
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
        bookings_data = view_bookings_action.view_bookings_action(customer_id)
        if bookings_data:
            for index, booking in enumerate(bookings_data):
                tree.insert("", index, text=str(index + 1), values=booking)

            
            tree.place(x=15, y=180, height=510, width=1230)
            
             # Add scrollbar to the treeview (vertical scrollbar)
            y_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=tree.yview)
            y_scrollbar.place(x=178 + 1050, y=182, height=506)

            # Add scrollbar to the treeview (horizontal scrollbar)
            x_scrollbar = ttk.Scrollbar(self.main_frame, orient="horizontal", command=tree.xview)
            x_scrollbar.place(x=15, y=687, width=1230)

            # Configure treeview to use scrollbars
            tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
   
        else:
            messagebox.showwarning("No Data", "No bookings data found.")



    def update_cancel_page(self, frame): 
        self.blabel = tk.Label(self.main_frame, image=self.photo_3)
        self.blabel.place(x=10, y=-375)
           
        self.lbl_1 = tk.Label(self.main_frame, width=33, text="Update/ Cancel Your Booking", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        self.lbl_1.place(x=590, y=50, height=85)
        
        self.lbl_frame = tk.Frame(self.main_frame, width=10000, bg="light gray")
        self.lbl_frame.place(x=-10, y=270, height=900)
        
        self.lbl_customer_id = tk.Label(self.main_frame, text="Customer ID: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_customer_id.place(x=50, y=330)
        self.txt_customer_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_customer_id.place(x=250, y=330, height=35)
        
        self.lbl_booking_id = tk.Label(self.main_frame, text="Booking ID: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_booking_id.place(x=700, y=330)
        self.txt_booking_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_booking_id.place(x=900, y=330, height=35)
        
        self.lbl_pick_up_address = tk.Label(self.main_frame, text="Pick Up Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_up_address.place(x=50, y=420)
        self.txt_pick_up_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_pick_up_address.place(x=250, y=420, height=35)
        
        self.lbl_drop_off_address = tk.Label(self.main_frame, text="Drop Off Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_drop_off_address.place(x=700, y=420)
        self.txt_drop_off_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_drop_off_address.place(x=900, y=420, height=35)
        
        self.lbl_pick_up_date = tk.Label(self.main_frame, text="Pick Up Date: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_up_date.place(x=50, y=510)
        update_today = datetime.now().date()
        update_tomorrow = update_today + timedelta(days=1)

        self.update_cal = DateEntry(self.main_frame, width=41, background='darkblue', foreground='white', borderwidth=2, year=update_today.year, month=update_today.month, day=update_today.day, font=("Candara", 10), mindate=update_today)
        self.update_cal.place(x=250, y=510, height=35)
        
        self.lbl_pick_up_time = tk.Label(self.main_frame, text="Pick Up Time: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_up_time.place(x=700, y=510)
        update_time_var = tk.StringVar()
        self.update_time_picker = ttk.Combobox(self.main_frame, width=22, textvariable=update_time_var, values=['12:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '08:00 AM', '9:00 AM', '10:00 AM', '11:00 AM','12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '04:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM'], font=("Candara", 17), state='readonly')
        self.update_time_picker.place(x=900, y=510, height=35)
        self.update_time_picker.set('08:00 AM')
        
        self.btn_update = tk.Button(self.main_frame, text="Update", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0, command=self.update_action)
        self.btn_update.place(x=330, y=610, height=50)
        
        self.btn_cancel = tk.Button(self.main_frame, text="Cancel Now!", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0, command=self.cancel_action)
        self.btn_cancel.place(x=980, y=610, height=50)

    def book_now_action(self):
        pick_address = self.txt_pick_address.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', pick_address):
            messagebox.showerror("Error", "Invalid Pick Up Address.")
            return
        
        drop_address = self.txt_drop_address.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', drop_address):
            messagebox.showerror("Error", "Invalid Drop Off Address.")
            return
    
        pick_date = self.cal.get_date()
       
        # Validate Time
        pick_time = self.time_picker.get()
        if not re.match(r'^\d{1,2}:\d{2} [APMapm]{2}$', pick_time):
            messagebox.showerror("Error", "Invalid Time.")
            return

        # Validate Checkbox
        agree = self.checkbox_var.get()
        if not agree:
            messagebox.showerror("Error", "You must agree to the terms.")
            return
        
        
        
        # ============================================================= DB ===========================================================================================================
        from book_now_action import book_now_action
        customer_id = global_all.global_customer_id
        result = book_now_action(pick_address, drop_address, pick_date, pick_time, agree, customer_id)
        
        if result:
            self.clear_entry_fields_1() 
    
    def update_action(self):
        up_customer_id = self.txt_customer_id.get()
        if not up_customer_id.isdigit():
            messagebox.showerror("Error", "Invalid Customer_ID.")
            return
        
        global_all.global_customer_id = up_customer_id
        
        up_booking_id = self.txt_booking_id.get()
        if not up_booking_id.isdigit():
            messagebox.showerror("Error", "Invalid Booking_ID.")
            return
        
        up_pick_up_address = self.txt_pick_up_address.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', up_pick_up_address):
            messagebox.showerror("Error", "Invalid Pick Up Address.")
            return
        
        up_drop_off_address = self.txt_drop_off_address.get()
        if not re.match(r'^[a-zA-Z0-9/-]+$', up_drop_off_address):
            messagebox.showerror("Error", "Invalid Pick Up Address.")
            return
        
        up_date = self.update_cal.get()
        
        up_time = self.update_time_picker.get()
        if not re.match(r'^\d{1,2}:\d{2} [APMapm]{2}$', up_time):
            messagebox.showerror("Error", "Invalid Time.")
            return
        
        from update_action import update_action
        result = update_action(up_customer_id, up_booking_id, up_pick_up_address, up_drop_off_address, up_date, up_time )
        
        if result:
            self.clear_entry_fields_2() 
    
    def cancel_action(self):
        cancel_customer_id = self.txt_customer_id.get()
        if not cancel_customer_id.isdigit():
            messagebox.showerror("Error", "Invalid Customer_ID.")
            return
        
        cancel_booking_id = self.txt_booking_id.get()
        if not cancel_booking_id.isdigit():
            messagebox.showerror("Error", "Invalid Booking_ID.")
            return
        
        from cancel_action import cancel_action
        result = cancel_action(cancel_customer_id, cancel_booking_id)
        
        if result:
            self.clear_entry_fields_2() 
        
    
    # Clear All Entries
    def clear_entry_fields_1(self):
        # Clear all entry fields
        self.txt_pick_address.delete(0, tk.END)
        self.txt_drop_address.delete(0, tk.END)
        self.checkbox_var.set(False)  # Uncheck the checkbox
    
    # Clear All Entries
    def clear_entry_fields_2(self):
        self.txt_customer_id.delete(0, tk.END)
        self.txt_booking_id.delete(0, tk.END)
        self.txt_pick_up_address.delete(0, tk.END)
        self.txt_drop_off_address.delete(0, tk.END)
    
    
if __name__ == '__main__':
    gui = Customer_dashboard()
    gui.mainloop()
