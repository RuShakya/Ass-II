from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


root = Tk()
root.title("Taxi Booking Login Page")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

image = Image.open("Ass-II/Views/image_1.webp")
photo = ImageTk.PhotoImage(image)

#gray_panel = tk.Frame(root, bg="gray", height=90, width=1000)
#gray_panel.grid(row=0, column=0, padx=10, pady=10)

alabel = Label(image=photo)
alabel.place(x=10, y=60)

lbl_title = Label(root, text="Taxi Booking System", width=60, font=("Times New Roman", 40, "italic"), fg="yellow", bg="gray")
lbl_title.place(x=10, y=10)

right_frame = Frame(root, bg="light gray", width=463, height=730)
right_frame.place(x=1050, y=90)  # Adjust the x-coordinate as needed


root.resizable(False, False)
root.mainloop()