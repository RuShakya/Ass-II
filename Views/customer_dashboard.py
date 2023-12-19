import tkinter as tk
from PIL import Image, ImageTk

class Customer_dashboard(tk.Tk):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.title("Taxi Booking Registration Page")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.resizable(False, False)
            
        self.lbl_dashboard = tk.Label(self, text="Customer Dashboard", width=25, font=("Times New Roman", 30, "italic"), fg="yellow", bg="gray")
        self.lbl_dashboard.place(x=0, y=0)

if __name__=='__main__':
    gui = Customer_dashboard()
    gui.mainloop()        
