import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk 
import re
import sys
sys.path.append('C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\Connection')
import conn
import register_action



class Customer_registration(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Registration Page")

        # database connection details
        from conn import conn
        self.db_connection = conn()
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")  
        self.resizable(False, False)
        self.image()
        self.heading()
        self.labels()
        self.buttons()
    

    def image(self):
        self.image1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_9.jpg")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.alabel = tk.Label(image=self.photo1, width=1100, anchor='e')
        self.alabel.place(x=-310, y=-160)
    
    def heading(self):    
        self.registration_frame1 = tk.Frame(self, bg="#F5F5DC", width=750, height=845)
        self.registration_frame1.place(x=790, y=0) 
        
        self.lbl_title = tk.Label(self, text="Register Now", width=55, font=("Times New Roman", 40, "bold"), fg="yellow", bg="black")
        self.lbl_title.place(x=-80, y=0, height=85)

    def labels(self):
        self.lbl_name = tk.Label(self, text="Name: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_name.place(x=900, y=160)
        self.txt_name = tk.Entry(self, width=28, font=("Candara", 15), bd=1)
        self.txt_name.place(x=1150, y=160, height=35)

        self.lbl_address = tk.Label(self, text="Address: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_address.place(x=900, y=230)
        self.txt_address = tk.Entry(self, width=28, font=("Candara", 15), bd=1)
        self.txt_address.place(x=1150, y=230, height=35)

        self.lbl_phone = tk.Label(self, text="Phone Number: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_phone.place(x=900, y=300)
        self.txt_phone = tk.Entry(self, width=28, font=("Candara", 15), bd=1)
        self.txt_phone.place(x=1150, y=300, height=35)

        self.lbl_email = tk.Label(self, text="Email Address: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_email.place(x=900, y=370)
        self.txt_email = tk.Entry(self, width=28, font=("Candara", 15), bd=1)
        self.txt_email.place(x=1150, y=370, height=35)

        self.lbl_username = tk.Label(self, text="Username: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_username.place(x=900, y=440)
        self.txt_username = tk.Entry(self, width=28, font=("Candara", 15), bd=1)
        self.txt_username.place(x=1150, y=440, height=35)

        self.lbl_password = tk.Label(self, text="Password: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_password.place(x=900, y=510)
        self.txt_password = tk.Entry(self, width=28, font=("Candara", 15), bd=1, show="*")
        self.txt_password.place(x=1150, y=510, height=35)
        
        self.show_password_var_1 = tk.IntVar()
        self.chk_show_password_1 = tk.Checkbutton(self, width=1, variable=self.show_password_var_1, command=self.toggle_password)
        self.chk_show_password_1.place(x=1427, y=511, height=34)

        self.lbl_confirmpw = tk.Label(self, text="Confirm Password: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_confirmpw.place(x=900, y=580)
        self.txt_confirmpw = tk.Entry(self, width=28, font=("Candara", 15), bd=1, show="*")
        self.txt_confirmpw.place(x=1150, y=580, height=35)
        
        self.show_password_var_2 = tk.IntVar()
        self.chk_show_password_2 = tk.Checkbutton(self, width=1, variable=self.show_password_var_2, command=self.toggle_password)
        self.chk_show_password_2.place(x=1427, y=581, height=34)

        self.lbl_payment = tk.Label(self, text="Payment Method: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_payment.place(x=900, y=650)
        self.payment_options = ["Cash", "Card"]
        self.payment_var = tk.StringVar()
        self.cmb_payment = ttk.Combobox(
        self, width=26, values=self.payment_options, textvariable=self.payment_var, font=("Candara", 15), state="readonly")
        self.cmb_payment.place(x=1150, y=650, height=35)
        self.cmb_payment.set("Cash")  # Set default value
        # Set font for the dropdown list
        self.cmb_payment.configure(font=("Candara", 15))
    
    def toggle_password(self):
        if self.show_password_var_1.get() == 1:
            self.txt_password.config(show="")
        else:
            self.txt_password.config(show="*")

        if self.show_password_var_2.get() == 1:
            self.txt_confirmpw.config(show="")
        else:
            self.txt_confirmpw.config(show="*")

    
    def go_to_login(self):
        self.destroy()
        from everyone_login import Everyone_login
        login_page = Everyone_login(self)
        login_page.mainloop()
    
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
        self.btn_back = tk.Button(self, text="Back", width=9, font=("Times New Roman", 20, "bold"), fg="black", bg="#F5F5DC", bd=0, command=self.go_to_login)
        self.btn_back.place(x=873, y=740, height=40)
        
        # Call the underline_text method with the button instance
        self.underline_text(self.btn_back)
        
        self.btn_register = tk.Button(self, text="Register", width=9, font=("Times New Roman", 20, "bold"), fg="white", bg="black", bd=1, command=self.register_button_action)
        self.btn_register.place(x=1305, y=740, height=40)


    def register_button_action(self):

        # Validation for name
        name = self.txt_name.get()
        if not name.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Name.")
            return
        
        # Validation for address
        address = self.txt_address.get()
        if not address.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Address.")
            return

        # Validation for phone 
        phone = self.txt_phone.get()
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Invalid Phone Number")
            return
        
        # Validation for email
        email = self.txt_email.get()
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
        
        confirm_password = self.txt_confirmpw.get()
        if confirm_password != password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        payment_method = self.cmb_payment.get()
        if not payment_method:
            messagebox.showerror("Error", "Invalid Payment Method.") 
            return 
        
        
        
        
        
        # DDDDDDDDDDDDDDDDDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        from register_action import register_action
        result = register_action(name, address, phone, email, username, password, confirm_password, payment_method)

        if result:
            self.destroy()
            from everyone_login import Everyone_login
            everyone_login_page = Everyone_login(self)
            everyone_login_page.mainloop()
    
    
           
if __name__=='__main__':
    gui = Customer_registration()
    gui.mainloop()