import tkinter as tk
from PIL import Image, ImageTk

class Everyone_login(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Login Page")
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        
        self.resizable(False, False)
        self.image()
        self.headings()
        self.labels()

    def image(self):
        self.image = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_1.webp")
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.alabel = tk.Label(image=self.photo)
        self.alabel.place(x=-30, y=75)

    def headings(self):
        self.lbl_title = tk.Label(self, text="Taxi Booking System", width=60, font=("Times New Roman", 40, "italic"), fg="yellow", bg="gray")
        self.lbl_title.place(x=-30, y=10, height=80)

        self.login_frame = tk.Frame(self, bg="light gray", width=563, height=745)
        self.login_frame.place(x=1010, y=105)  

        self.lbl_login = tk.Label(self, text="Login Page", width=25, font=("Times New Roman", 30, "italic"), fg="yellow", bg="gray")
        self.lbl_login.place(x=1010, y=150)

    def labels(self):
        self.lbl_username = tk.Label(self, text="Username: ", width=10, font=("Calibri", 15), bg="light gray")
        self.lbl_username.place(x=1100, y=290)
        self.txt_username = tk.Entry(self, width=30, font=("Calibri", 11), bd=1)
        self.txt_username.place(x=1220, y=290, height=30)

        self.lbl_password = tk.Label(self, text="Password: ", width=10, font=("Calibri", 15), bg="light gray")
        self.lbl_password.place(x=1100, y=350)
        self.txt_password = tk.Entry(self, width=30, font=("Calibri", 11), bd=1)
        self.txt_password.place(x=1220, y=350, height=30)

        self.lbl_register = tk.Label(self, text="If you have not register yet?? ", width=23, font=("Calibri", 12, "italic"), bg="light gray")
        self.lbl_register.place(x=1120, y=410)

        self.btn_clkhere = tk.Button(self, text="Click Here to Register", width=17, font=("Calibri, 12"), fg="gray", bg="light gray", bd=0)
        self.btn_clkhere.place(x=1315, y=408)

        self.btn_login = tk.Button(self, text="Login", width=15, font=("Calibri, 15"), fg="white", bg="black", bd=0)
        self.btn_login.place(x=1330, y=490)


    
if __name__=='__main__':
    gui = Everyone_login()
    gui.mainloop()