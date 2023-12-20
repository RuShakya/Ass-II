import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Frame Switching Example")

        self.frames = {}

        # Create and add frames to the dictionary
        for F in (Frame1, Frame2, Frame3):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Frame1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Frame1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Frame 1", font=('Helvetica', 18))
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Open Frame 2", command=lambda: master.show_frame(Frame2))
        button.pack(pady=10)

class Frame2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Frame 2", font=('Helvetica', 18))
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Open Frame 1", command=lambda: master.show_frame(Frame1))
        button1.pack(pady=5)

        button3 = tk.Button(self, text="Open Frame 3", command=lambda: master.show_frame(Frame3))
        button3.pack(pady=5)

class Frame3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Frame 3", font=('Helvetica', 18))
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Open Frame 2", command=lambda: master.show_frame(Frame2))
        button2.pack(pady=5)

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("400x300")
    app.mainloop()
