import tkinter as tk
from PIL import Image, ImageTk

class Admin_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Admin Dashboard Page")

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
        

    def home_page(self, frame):   
        self.alabel = tk.Label(self.main_frame, image=self.photo_1)
        self.alabel.place(x=-10, y=-550)
                     
        lbl_1 = tk.Label(self.main_frame, width=30, text="Ensuring A Seemless Experience", font=("Candara", 30, "bold"), fg="black", bg="light gray", bd=1)
        lbl_1.place(x=600, y=510, height=65)
        
        lbl_2 = tk.Label(self.main_frame, width=25, text=" Control Without Complexity", font=("Candara", 30, "bold"), fg="black", bg="light gray")
        lbl_2.place(x=710, y=610, height=65)
        

    def manage_drivers_page(self, frame):    
        lbl_1 = tk.Label(self.main_frame, width=20, text="Manage Drivers", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=830, y=60, height=65)
        
        lbl_frame = tk.Frame(self.main_frame, width=10000, bg="light gray")
        lbl_frame.place(x=-10, y=185, height=900)
        
        lbl_driver_name = tk.Label(self.main_frame, text="Driver's Name: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_driver_name.place(x=50, y=250)
        txt_driver_name = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_driver_name.place(x=250, y=250, height=35)
        
        lbl_driver_address = tk.Label(self.main_frame, text="Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_driver_address.place(x=700, y=250)
        txt_driver_address = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_driver_address.place(x=900, y=250, height=35)
        
        lbl_driver_mobile = tk.Label(self.main_frame, text="Mobile: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_driver_mobile.place(x=50, y=350)
        txt_driver_mobile = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_driver_mobile.place(x=250, y=350, height=35)
        
        lbl_driver_email = tk.Label(self.main_frame, text="Email Address: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_driver_email.place(x=700, y=350)
        txt_driver_email = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_driver_email.place(x=900, y=350, height=35)
        
        lbl_username = tk.Label(self.main_frame, text="Username: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_username.place(x=50, y=450)
        txt_username = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_username.place(x=250, y=450, height=35)
        
        lbl_password = tk.Label(self.main_frame, text="Password: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_password.place(x=700, y=450)
        txt_password = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_password.place(x=900, y=450, height=35)
        
        lbl_licence_number = tk.Label(self.main_frame, text="Licence Number: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_licence_number.place(x=50, y=550)
        txt_licence_number = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_licence_number.place(x=250, y=550, height=35)
        
        lbl_taxi_plate_number = tk.Label(self.main_frame, text="Taxi Plate Number: ", font=("Candara", 17), fg="black", bg="light gray", anchor="e")
        lbl_taxi_plate_number.place(x=700, y=550)
        txt_taxi_plate_number = tk.Entry(self.main_frame, width=28, font=("Candara", 15), bd=1)
        txt_taxi_plate_number.place(x=900, y=550, height=35)
        
        btn_book_now = tk.Button(self.main_frame, text="Add Driver", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0)
        btn_book_now.place(x=330, y=640, height=50)
        
        btn_book_now = tk.Button(self.main_frame, text="Delete Driver", width=15, font=("Candara", 20, "bold"), fg="black", bg="yellow", bd=0)
        btn_book_now.place(x=980, y=640, height=50)
        
        

    def view_drivers_page(self, frame):
        lbl_1 = tk.Label(self.main_frame, width=20, text="View Drivers", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=90, height=65)


    def manage_bookings_page(self, frame): 
        lbl_1 = tk.Label(self.main_frame, width=20, text="Manage Bookings", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=90, height=65)
        
    
    def customers_details_page(self, frame): 
        lbl_1 = tk.Label(self.main_frame, width=20, text="Customers Details", font=("Candara", 30, "bold"), fg="white", bg="brown", bd=1)
        lbl_1.place(x=844, y=90, height=65)
        
    

if __name__ == '__main__':
    gui = Admin_dashboard()
    gui.mainloop()
    
    
    
    
    
    
    
    
    
    
    