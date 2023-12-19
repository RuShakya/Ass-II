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

        self.image1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_4.webp")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.alabel = tk.Label(image=self.photo1)
        self.alabel.place(x=45, y=150)
        
        self.registration_frame1 = tk.Frame(self, bg="#F5F5DC", width=490, height=845)
        self.registration_frame1.place(x=700, y=0) 

        self.registration_frame2 = tk.Frame(self, bg="#F5F5DC", width=553, height=845)
        self.registration_frame2.place(x=1130, y=0)  
        
        self.lbl_title = tk.Label(self, text="Register Now", width=60, font=("Times New Roman", 40, "italic"), fg="white", bg="black")
        self.lbl_title.place(x=-80, y=0, height=85)

        self.lbl_name = tk.Label(self, text="Name: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_name.place(x=910, y=160)
        self.txt_name = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_name.place(x=1150, y=160, height=35)

        self.lbl_address = tk.Label(self, text="Address: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_address.place(x=910, y=230)
        self.txt_address = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_address.place(x=1150, y=230, height=35)

        self.lbl_phone = tk.Label(self, text="Phone Number: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_phone.place(x=910, y=300)
        self.txt_phone = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_phone.place(x=1150, y=300, height=35)

        self.lbl_email = tk.Label(self, text="Email Address: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_email.place(x=910, y=370)
        self.txt_email = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_email.place(x=1150, y=370, height=35)

        self.lbl_username = tk.Label(self, text="Username: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_username.place(x=910, y=440)
        self.txt_username = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_username.place(x=1150, y=440, height=35)

        self.lbl_password = tk.Label(self, text="Password: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_password.place(x=910, y=510)
        self.txt_password = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_password.place(x=1150, y=510, height=35)

        self.lbl_confirmpw = tk.Label(self, text="Confirm Password: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_confirmpw.place(x=910, y=580)
        self.txt_confirmpw = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_confirmpw.place(x=1150, y=580, height=35)

        self.lbl_payment = tk.Label(self, text="Payment Method: ", width=17, font=("Candara", 17), bg="#F5F5DC", anchor='e')
        self.lbl_payment.place(x=910, y=650)
        self.txt_payment = tk.Entry(self, width=38, font=("Candara", 11), bd=1)
        self.txt_payment.place(x=1150, y=650, height=35)

        self.btn_back = tk.Button(self, text="<<", width=3, font=("Times New Roman", 20, "italic"), fg="black", bg="white", bd=5)
        self.btn_back.place(x=40, y=23, height=37)

        self.btn_register = tk.Button(self, text="Register", width=9, font=("Times New Roman", 20, "italic"), fg="white", bg="black", bd=5)
        self.btn_register.place(x=1290, y=750, height=50)

        
if __name__=='__main__':
    gui = Customer_registration()
    gui.mainloop()