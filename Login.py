from tkinter import *
from tkinter import messagebox
import tkinter as tk
from Register import *
from Recovery import *
from Main import *
from Settings import *

class Login:
#Creating new window
#logLab  - Label for “login”
#logEnt  - Entry for username
#passLab  - Label for “password”
#passEnt - Entry for password
#logBtn - Button for authentication
#regBtn - Button that creates new form for registration new account
#recBtn - Button that creates new form for recovering account
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Login')

        self.logLab = Label(self.master, text = 'Login', bg = 'white', font = 'Verden 14')
        self.logEnt = Entry(self.master)
        self.logLab.grid(row = 1, column = 1)
        self.logEnt.grid(row = 1, column = 3)

        self.passLab = Label(self.master, text = 'Password', bg = 'white', font = 'Verden 14')
        self.passEnt = Entry(self.master)
        self.passLab.grid(row = 2, column = 1)
        self.passEnt.grid(row = 2, column = 3)

        self.logBtn = Button(self.master, text = 'Login', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.logOnClick)
        self.regBtn = Button(self.master, text = 'Register', width = 20, bg = 'green', font = 'Verden 14', fg = 'white', command = self.regOnClick)
        self.recBtn = Button(self.master, text = 'Forgot password or login', width = 20, bg = 'red', font = 'Verden 14', fg = 'white', command = self.recOnClick)
        self.logBtn.grid(row = 3, column = 1, columnspan = 3)
        self.regBtn.grid(row = 4, column = 1, columnspan = 3)
        self.recBtn.grid(row = 5, column = 1, columnspan = 3)

#verification algorithm
#logPass - variable that stores all account information
#login - variable that copies data from logEnt
#password - variable that copies data from passEnt
    def verify(self):
        file = open('regDB.txt', 'r')
        logPass = file.read()

        login = self.logEnt.get()
        password = self.passEnt.get()

        if login is '' or password is '':
            return False

        for i in range(len(logPass)):
            if logPass[i:i+4] == 'Name:':
                i += 4
                continue
            else:
                if logPass[i:i+len(login)] == login:
                    if logPass[i+len(login)+11:i+len(login)+11+len(password)] == password:
                        return True

                if logPass[i:i+len(login)] != login:
                    while logPass[i] != '\n':
                        i += 1

                if i == len(logPass):
                    return False

#algorithm that opens Registration window
#newWindow - priority to new window
#app - creating new window
    def regOnClick(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Register(self.newWindow)

#algorithm that opens Main window
#newWindow - priority to new window
#app - creating new window
    def logOnClick(self):
        if self.verify():
            self.newWindow = tk.Toplevel(self.master)
            self.app = Main(self.newWindow, self.logEnt.get(), self.passEnt.get())
            self.master.withdraw()
        else:
            messagebox.showerror('Error', 'Invalid login or password')

#algorithm that opens Recovery window
#newWindow - priority to new window
#app - creating new window
    def recOnClick(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Recovery(self.newWindow)

