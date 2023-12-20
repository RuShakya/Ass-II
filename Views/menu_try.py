import tkinter as tk

def menu_command():
    print("Menu item clicked")

# Create the main window
root = tk.Tk()
root.title("Vertical Menu")

# Create a menu
menu = tk.Menu(root)

# Add menu items
menu.add_command(label="Item 1", command=menu_command)
menu.add_command(label="Item 2", command=menu_command)
menu.add_command(label="Item 3", command=menu_command)
menu.add_command(label="Item 4", command=menu_command)
menu.add_command(label="Item 5", command=menu_command)

# Attach the menu to the root window
root.config(menu=menu)

# Set up geometry for the menu items (vertical alignment on the left)
for item in menu.winfo_children():
    item.pack(side=tk.LEFT, fill=tk.Y)

# Start the Tkinter event loop
root.mainloop()
