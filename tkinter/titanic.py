import tkinter as tk
from tkinter.messagebox import showwarning
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.titanic = Image.open("titanic.png")
        self.titanic2 = Image.open("titanic2.png")
        self.pack()
        self.create_widgets()

    def send_sos(self):
        showwarning(title="S.O.S.", message="we are sinking")

    def collision(self):
        photo = ImageTk.PhotoImage(self.titanic2)
        self.canvas.image = photo
        self.im = self.canvas.create_image(0, 0, image=photo, anchor='nw')

    def create_widgets(self):
        photo = ImageTk.PhotoImage(self.titanic)
        self.canvas = tk.Canvas(self, width=700, height=178, bg='black')
        self.canvas.pack(side='top', fill='both', expand='yes')
        self.canvas.image = photo # keep a reference!
        self.im = self.canvas.create_image(0, 0, image=photo, anchor='nw')

        self.quit = tk.Button(self, text="Abandon ship",
                              command=root.destroy)
        self.quit.pack(side="bottom", fill="both", expand="yes")

        self.sos = tk.Button(self, fg="red")
        self.sos["text"] = "Send out S.O.S."
        self.sos["command"] = self.send_sos
        self.sos.pack(side="bottom", fill="both", expand="yes")

        self.sink = tk.Button(self)
        self.sink["text"] = "Full Speed"
        self.sink["command"] = self.collision
        self.sink.pack(side="bottom", fill="both", expand="yes")



root = tk.Tk()
app = Application(master=root)
app.master.title("Titanic-Simulator 1.0")
app.mainloop()
