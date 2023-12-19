import tkinter as tk
from PIL import Image, ImageTk

class Customer_registration(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Registration Page")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")  
        self.resizable(False, False)
        self.image()
        self.heading()
        self.labels()
        self.buttons()
    
        
    def image(self):
        self.image1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_905.jpg")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.alabel = tk.Label(image=self.photo1, width=1100, anchor='e')
        self.alabel.place(x=-310, y=-160)
    
    def heading(self):    
        self.registration_frame1 = tk.Frame(self, bg="#F5F5DC", width=750, height=845)
        self.registration_frame1.place(x=790, y=0) 
        
        self.lbl_title = tk.Label(self, text="Register Now", width=60, font=("Times New Roman", 40, "italic"), fg="white", bg="black")
        self.lbl_title.place(x=-80, y=0, height=85)

    def labels(self):
        self.lbl_name = tk.Label(self, text="Name: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_name.place(x=900, y=160)
        self.txt_name = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_name.place(x=1150, y=160, height=35)

        self.lbl_address = tk.Label(self, text="Address: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_address.place(x=900, y=230)
        self.txt_address = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_address.place(x=1150, y=230, height=35)

        self.lbl_phone = tk.Label(self, text="Phone Number: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_phone.place(x=900, y=300)
        self.txt_phone = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_phone.place(x=1150, y=300, height=35)

        self.lbl_email = tk.Label(self, text="Email Address: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_email.place(x=900, y=370)
        self.txt_email = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_email.place(x=1150, y=370, height=35)

        self.lbl_username = tk.Label(self, text="Username: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_username.place(x=900, y=440)
        self.txt_username = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_username.place(x=1150, y=440, height=35)

        self.lbl_password = tk.Label(self, text="Password: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_password.place(x=900, y=510)
        self.txt_password = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_password.place(x=1150, y=510, height=35)

        self.lbl_confirmpw = tk.Label(self, text="Confirm Password: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_confirmpw.place(x=900, y=580)
        self.txt_confirmpw = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_confirmpw.place(x=1150, y=580, height=35)

        self.lbl_payment = tk.Label(self, text="Payment Method: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_payment.place(x=900, y=650)
        self.txt_payment = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_payment.place(x=1150, y=650, height=35)
    
    
    def go_to_login(self):
        self.destroy()
        from everyone_login import Everyone_login
        login_page = Everyone_login(self)
        login_page.mainloop()
    
    def buttons(self):
        self.btn_back = tk.Button(self, text="<< Back", width=9, font=("Times New Roman", 20, "italic"), fg="white", bg="black", bd=1, command=self.go_to_login)
        self.btn_back.place(x=840, y=740, height=45)

        self.btn_register = tk.Button(self, text="Register", width=9, font=("Times New Roman", 20, "italic"), fg="white", bg="black", bd=1)
        self.btn_register.place(x=1335, y=740, height=45)

    
    
           
if __name__=='__main__':
    gui = Customer_registration()
    gui.mainloop()