from tkinter import *
from Login import *
import tkinter as tk

class Launch:
#Opens new Login window
    def __init__(self):
        window = tk.Tk()
        app = Login(window)
        window.mainloop()

if __name__ == '__main__':
#executes Launch class
    Launch()
