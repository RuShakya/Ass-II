
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox 
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Views')
import global_all
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Connection')
import view_driver_bookings_action
import trip_completed_action

class Driver_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Syatem Driver Dashboard Page")
        
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
        self.image_1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_23.jpg")
        self.photo_1 = ImageTk.PhotoImage(self.image_1)   
        
    def headings(self):
        self.lbl_title1 = tk.Label(self, width=8, bg="#02211f", anchor="w")
        self.lbl_title1.place(x=-20, y=0, height=90)

        self.lbl_title2 = tk.Label(self, text="Driver Dashboard", width=50, font=("Times New Roman", 40, "bold"), fg="yellow", bg="#02211f", anchor="w")
        self.lbl_title2.place(x=40, y=0, height=90)

        self.lbl_welcome = tk.Label(self, text="Welcome", width=10, font=("Candara", 38, "bold"), fg="white", bg="#02211f", anchor="e")
        self.lbl_welcome.place(x=1190, y=0, height=90)

        self.lbl_side = tk.Label(self, width=38, bg="#02211f", anchor="w")
        self.lbl_side.place(x=-2, y=90, height=900)    

    def frames(self):
        self.main_frame = tk.Frame(self, highlightbackground="#02211f", highlightthickness=0)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1268, height=790)
        self.main_frame.place(x=271, y=90)
        
    
    def hide_indicators(self):
        self.home_indicate.config(bg="#02211f")
        self.view_indicate.config(bg="#02211f")
        
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
        self.btn_home = tk.Button(self, text="Home", width=15, font=("Candara", 23, "bold"), fg="white", bg="#02211f", bd=0, command=lambda: self.indicate(self.home_indicate, self.home_page))
        self.btn_home.place(x=-2, y=190, height=40)

        # Home_Indicator
        self.home_indicate = tk.Label(self, text=" ", bg="black")
        self.home_indicate.place(x=0, y=190, width=10, height=40)
    
        # View Button
        self.btn_view = tk.Button(self, text="View Bookings", width=15, font=("Candara", 23, "bold"), fg="white", bg="#02211f", bd=0, command=lambda: self.indicate(self.view_indicate, self.view_page))
        self.btn_view.place(x=-2, y=350, height=40)

        # View_Indicator
        self.view_indicate = tk.Label(self, text=" ", bg="black")
        self.view_indicate.place(x=0, y=350, width=10, height=40)    
    
    
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
        
    
    def on_treeview_select(self, event):
        # Get the selected item in the Treeview
        item = event.widget.selection()[0]
        values = event.widget.item(item, "values")

        # Extract customer_id and booking_id from the selected row
        customer_id, booking_id, driver_id = values[0], values[3], values[9]

        # Set the values in the corresponding entry fields
        self.txt_customer_id.delete(0, tk.END)
        self.txt_customer_id.insert(0, customer_id)

        self.txt_booking_id.delete(0, tk.END)
        self.txt_booking_id.insert(0, booking_id)
        
        self.txt_driver_id.delete(0, tk.END)
        self.txt_driver_id.insert(0, driver_id)
     
        
    def home_page(self, frame): 
        self.alabel = tk.Label(self.main_frame, image=self.photo_1)
        self.alabel.place(x=-10, y=-5)
        
        self.lbl_1 = tk.Label(self.main_frame, width=25, text="Safe travels, Smooth rides", font=("Candara", 30, "bold"), fg="white", bg="#4a967a", bd=1)
        self.lbl_1.place(x=700, y=90, height=65)
        
        self.lbl_2 = tk.Label(self.main_frame, width=20, text="Cherish Every Mile", font=("Candara", 30, "bold"), fg="white", bg="#4a967a")
        self.lbl_2.place(x=825, y=190, height=65)
        
        self.btn_logout = tk.Button(self.main_frame, text="Log Out", width=13, font=("Candara", 23, "bold"), fg="black", bg="yellow", command=self.go_to_everyone_login)
        self.btn_logout.place(x=990, y=650, height=50)
        
    
    def view_page(self, frame):
        driver_id = global_all.global_driver_id  # Fetch the driver ID from the global variable
        
        self.lbl_1 = tk.Label(self.main_frame, width=33, text="View Your Bookings", font=("Candara", 30, "bold"), fg="white", bg="#4a967a", bd=1)
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
        bookings_data = view_driver_bookings_action.view_driver_bookings_action(driver_id)
        if bookings_data:
            for index, booking in enumerate(bookings_data):
                tree.insert("", index, text=str(index + 1), values=booking)

            # Add a binding to the Treeview selection event
            tree.bind("<ButtonRelease-1>", self.on_treeview_select)
            
            tree.place(x=15, y=180, height=260, width=1230)
            
             # Add scrollbar to the treeview (vertical scrollbar)
            y_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=tree.yview)
            y_scrollbar.place(x=178 + 1050, y=182, height=258)

            # Add scrollbar to the treeview (horizontal scrollbar)
            x_scrollbar = ttk.Scrollbar(self.main_frame, orient="horizontal", command=tree.xview)
            x_scrollbar.place(x=15, y=440, width=1230)

            # Configure treeview to use scrollbars
            tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
   
        else:
            messagebox.showwarning("No Data", "No bookings data found.")
        
        self.lbl_customer_id = tk.Label(self.main_frame, text="Customer ID: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_customer_id.place(x=50, y=500)
        self.txt_customer_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_customer_id.place(x=220, y=500, height=35)
        
        self.lbl_booking_id = tk.Label(self.main_frame, text="Booking ID: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_booking_id.place(x=730, y=500)
        self.txt_booking_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_booking_id.place(x=900, y=500, height=35)
        
        self.lbl_driver_id = tk.Label(self.main_frame, text="Driver ID: ", font=("Candara", 17), fg="black", anchor="e")
        self.lbl_driver_id.place(x=50, y=600)
        self.txt_driver_id = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        self.txt_driver_id.place(x=220, y=600, height=35)
        
        self.btn_trip_completed = tk.Button(self.main_frame, text="Trip Completed", width=13, font=("Candara", 23, "bold"), fg="white", bg="#4a967a", command=self.trip_completed_action)
        self.btn_trip_completed.place(x=986, y=650, height=50)
        
    
    def trip_completed_action(self):
        
        customer_id = self.txt_customer_id.get()
        booking_id = self.txt_booking_id.get()
        driver_id = self.txt_driver_id.get()
        
        # Validate input data
        if not customer_id.isdigit() or not booking_id.isdigit() or not driver_id.isdigit():
            messagebox.showerror("Error", "Invalid input. Please enter valid ID.")
            return
        
        # Ask for confirmation using a messagebox
        confirm = messagebox.askyesno("Confirmation", "Are you sure the trip is completed?")
        
        if confirm:
            # Proceed with the action if the user clicks 'Yes'
            from trip_completed_action import trip_completed_action
            result = trip_completed_action(
                customer_id,
                booking_id,
                driver_id,
                'Completed',
                'Available'
            )
               
            if result:
                messagebox.showinfo("Great Job", "Trip Completed Successfully!")
            else:
                messagebox.showinfo("No Trip Completed", "No Trip Completed.")
                
        else:
            # Do nothing or handle the case where the user clicks 'No'
            pass




    

if __name__ == "__main__":
    driver_gui = Driver_dashboard()
    driver_gui.mainloop()