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

class Customer_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Customer Dasgboard Page")

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


    def home_page(self, frame):        
        self.alabel = tk.Label(self.main_frame, image=self.photo_1)
        self.alabel.place(x=-1, y=-500)
        
        self.lbl_1 = tk.Label(self.main_frame, width=20, text="Tap, Book, Roll", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        self.lbl_1.place(x=844, y=90, height=65)
        
        self.lbl_2 = tk.Label(self.main_frame, width=25, text=" Your Cozy Ride Awaits!", font=("Candara", 30, "bold"), fg="white", bg="brown")
        self.lbl_2.place(x=710, y=190, height=65)
        

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

        self.cal = DateEntry(self.main_frame, width=32, background='darkblue', foreground='white', borderwidth=2, year=today.year, month=today.month, day=today.day, font=("Candara", 12), mindate=today)
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
        self.lbl = tk.Label(self.main_frame, text="View Page", font=("Candara", 16))
        self.lbl.pack()

    def update_cancel_page(self, frame): 
        self.blabel = tk.Label(self.main_frame, image=self.photo_3)
        self.blabel.place(x=10, y=-375)
           
        self.lbl_1 = tk.Label(self.main_frame, width=33, text="Update/ Cancel Your Booking", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        self.lbl_1.place(x=590, y=50, height=85)
        
        self.lbl_frame = tk.Frame(self.main_frame, width=10000, bg="light gray")
        self.lbl_frame.place(x=-10, y=270, height=900)
        
        self.lbl_customer_id = tk.Label(self.main_frame, text="Customer ID: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_customer_id.place(x=50, y=320)
        self.txt_customer_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_customer_id.place(x=250, y=320, height=35)
        
        self.lbl_booking_id = tk.Label(self.main_frame, text="Booking ID: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_booking_id.place(x=700, y=320)
        self.txt_booking_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_booking_id.place(x=900, y=320, height=35)
        
        self.lbl_pick_up_address = tk.Label(self.main_frame, text="Pick Up Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_up_address.place(x=50, y=410)
        self.txt_pick_up_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_pick_up_address.place(x=250, y=410, height=35)
        
        self.lbl_drop_off_address = tk.Label(self.main_frame, text="Drop Off Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_drop_off_address.place(x=700, y=410)
        self.txt_drop_off_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_drop_off_address.place(x=900, y=410, height=35)
        
        self.lbl_pick_date = tk.Label(self.main_frame, text="Pick Up Date: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_date.place(x=50, y=500)
        self.txt_pick_date = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_pick_date.place(x=250, y=500, height=35)
        
        self.lbl_pick_time = tk.Label(self.main_frame, text="Pick Up Time: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        self.lbl_pick_time.place(x=700, y=500)
        self.txt_pick_time = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_pick_time.place(x=900, y=500, height=35)
        
        self.btn_update = tk.Button(self.main_frame, text="Update", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0)
        self.btn_update.place(x=330, y=600, height=50)
        
        self.btn_cancel = tk.Button(self.main_frame, text="Cancel Now!", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0)
        self.btn_cancel.place(x=980, y=600, height=50)

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
        
        # DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        from book_now_action import book_now_action
        result = book_now_action(pick_address, drop_address, pick_date, pick_time, agree)
        
        if result:
            self.clear_entry_fields() 
    
    # Clear All Entries
    def clear_entry_fields(self):
        # Clear all entry fields
        self.txt_pick_address.delete(0, tk.END)
        self.txt_drop_address.delete(0, tk.END)
        self.checkbox_var.set(False)  # Uncheck the checkbox
    
    
if __name__ == '__main__':
    gui = Customer_dashboard()
    gui.mainloop()
