from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry('1000x1000')

image = Image.open("Ass-II/Views/image_2.jpg")
photo = ImageTk.PhotoImage(image)

alabel = Label(image=photo)
alabel.pack()

root.mainloop()