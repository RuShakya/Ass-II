import tkinter as tk
from PIL import Image, ImageTk

class Customer_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Registration Page")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.resizable(False, False)
        self.image()
        self.headings()
        self.frames()
        self.buttons_indicators()
        self.hide_indicators()
        # Automatically open the home page
        self.indicate(self.home_indicate, self.home_page)

    def image(self):
        self.image1 = Image.open("C:\\Users\\user\\Desktop\\Sem 2 - Assignment 2\\Ass-II\\ZImage\\image_114.jpg")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.alabel = tk.Label(image=self.photo1)
        self.alabel.place(x=350, y=-88)

    def headings(self):
        self.lbl_title1 = tk.Label(self, width=8, bg="black", anchor="w")
        self.lbl_title1.place(x=-20, y=0, height=90)

        self.lbl_title2 = tk.Label(self, text="Customer Dashboard", width=50, font=("Times New Roman", 40, "bold"), fg="yellow", bg="black", anchor="w")
        self.lbl_title2.place(x=40, y=0, height=90)

        self.lbl_title2 = tk.Label(self, text="Welcome", width=10, font=("Candara", 38, "bold"), fg="white", bg="black", anchor="e")
        self.lbl_title2.place(x=1190, y=0, height=90)

        self.lbl_side = tk.Label(self, width=38, bg="black", anchor="w")
        self.lbl_side.place(x=-2, y=90, height=900)

    def frames(self):
        self.main_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1260, height=751)
        self.main_frame.place(x=270, y=90)

    def hide_indicators(self):
        self.home_indicate.config(bg="black")
        # Add other indicators as needed
        self.book_indicate.config(bg="black")
        self.view_indicate.config(bg="black")
        self.update_cancel_indicate.config(bg="black")

    def indicate(self, lb, page):
        self.hide_indicators()
        lb.config(bg="yellow")
        page()

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

    def home_page(self):
        home_frame = tk.Frame(self.main_frame)
        lbl = tk.Label(home_frame, text="Home Page", font=("Candara", 16))
        lbl.pack()
        home_frame.pack(pady=20)
        
    def book_page(self):
        book_frame = tk.Frame(self.main_frame)
        lbl = tk.Label(book_frame, text="Book Page", font=("Candara", 16))
        lbl.pack()
        book_frame.pack(pady=20)

    def view_page(self):
        view_frame = tk.Frame(self.main_frame)
        lbl = tk.Label(view_frame, text="View Page", font=("Candara", 16))
        lbl.pack()
        view_frame.pack(pady=20)

    def update_cancel_page(self):
        update_cancel_frame = tk.Frame(self.main_frame)
        lbl = tk.Label(update_cancel_frame, text="Update/Cancel Page", font=("Candara", 16))
        lbl.pack()
        update_cancel_frame.pack(pady=20)
        
        

if __name__ == '__main__':
    gui = Customer_dashboard()
    gui.mainloop()
