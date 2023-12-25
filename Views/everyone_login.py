import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Connection')
import conn
import login_action

class Everyone_login(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Login Page")
        
        # database connection details
        from conn import conn
        self.db_connection = conn()
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
    
        self.resizable(False, False)
        self.image()
        self.headings()
        self.labels()
        self.buttons()
        self.toggle_password()

    def image(self):
        self.image = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_1.webp")
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.alabel = tk.Label(image=self.photo)
        self.alabel.place(x=-30, y=75)

    def headings(self):
        self.lbl_title = tk.Label(self, text="Taxi Booking System", width=50, font=("Times New Roman", 40, "bold"), fg="yellow", bg="black")
        self.lbl_title.place(x=-30, y=10, height=80)

        self.login_frame = tk.Frame(self, bg="light gray", width=563, height=745)
        self.login_frame.place(x=1010, y=105)  

        self.lbl_login = tk.Label(self, text="Login Page", width=23, font=("Times New Roman", 30, "bold"), fg="yellow", bg="black")
        self.lbl_login.place(x=1010, y=150)

    def labels(self):
        self.lbl_username = tk.Label(self, text="Username: ", width=10, font=("Candara", 17), bg="light gray")
        self.lbl_username.place(x=1100, y=290)
        self.txt_username = tk.Entry(self, width=20, font=("Candara", 15), bd=1)
        self.txt_username.place(x=1230, y=290, height=35)

        self.lbl_password = tk.Label(self, text="Password: ", width=10, font=("Candara", 17), bg="light gray")
        self.lbl_password.place(x=1100, y=360)
        self.txt_password = tk.Entry(self, width=20, font=("Candara", 15), bd=1, show="*")
        self.txt_password.place(x=1230, y=360, height=35)
        
        self.show_password_var = tk.IntVar()
        self.chk_show_password = tk.Checkbutton(self, width=1, variable=self.show_password_var, command=self.toggle_password)
        self.chk_show_password.place(x=1419, y=361, height=34)

        self.lbl_register = tk.Label(self, text="If you have not registered yet?? ", width=25, font=("Candara", 12, "italic"), bg="light gray")
        self.lbl_register.place(x=1117, y=430)
        
    def toggle_password(self):
        if self.show_password_var.get() == 1:
            self.txt_password.config(show="")
        else:
            self.txt_password.config(show="*")

    def go_to_registration(self):
        self.destroy()
        from customer_registration import Customer_registration
        registration_page = Customer_registration(self)
        registration_page.mainloop()
    
    def go_to_customer_dashboard(self):
        self.destroy()
        from customer_dashboard import Customer_dashboard
        customer_dashboard_page = Customer_dashboard(self)
        customer_dashboard_page.mainloop()
    
    def go_to_admin_dashboard(self):
        self.destroy()
        from admin_dashboard import Admin_dashboard
        admin_dashboard_page = Admin_dashboard(self)
        admin_dashboard_page.mainloop()
    
    def underline_text(self, button):
        from tkinter import font

        # Get the current font of the button
        current_font = button.cget("font")

        # Create a Font object with the underline attribute set to True
        underlined_font = font.Font(font=current_font)
        underlined_font.configure(underline=True)

        # Apply the underlined font to the button
        button.configure(font=underlined_font)

    
    def buttons(self):
        self.btn_clkhere = tk.Button(self, text="Sign Up", width=10, font=("Times New Roman", 15, "bold"), fg="gray", bg="light gray", bd=0, anchor='w', command=self.go_to_registration)
        self.btn_clkhere.place(x=1325, y=425)
        
        # Call the underline_text method with the button instance
        self.underline_text(self.btn_clkhere)

        self.btn_login = tk.Button(self, text="Login", width=8, font=("Times New Roman", 20, "bold"), fg="white", bg="black", bd=0, command=self.login_button_action)
        self.btn_login.place(x=1325, y=500, height=40)

    
    def login_button_action(self):

        username = self.txt_username.get()
        password = self.txt_password.get()
        
        from login_action import login_action
        result = login_action(username, password)
        if result == "customer":
            self.go_to_customer_dashboard()
        elif result == "admin":
            self.go_to_admin_dashboard()
 
        
    
if __name__=='__main__':
    gui = Everyone_login()
    gui.mainloop()