import tkinter as tk
from playsound import playsound
import random
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("300x50")
        self.winfo_toplevel().title("Ooga Ooga")
        tk.Button(self, text="Go Monke", command = lambda: playsound('monkey' + str(random.randint(1, 4)) + ".mp3", block = False)).pack()

app = SampleApp()
app.mainloop()
