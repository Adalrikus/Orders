from tkinter import *
from tkinter import messagebox
import tkinter as tk
import fileinput

class Settings:
    def __init__(self, master, user, password):
        self.master = master
        self.user = user
        self.password = password
        self.frame = Frame(self.master)
        self.master.title('Settings')
        self.master.configure(background = 'white')

        self.usrLab = Label(self.master, text = 'Username: ', bg = 'white', font = 'Verden 14')
        self.usrEnt = Entry(self.master)
        self.usrEnt.insert(0, self.user)
        self.usrLab.grid(row = 1, column = 1)
        self.usrEnt.grid(row = 1, column = 2)

        self.passLab = Label(self.master, text = 'Password: ', bg = 'white', font = 'Verden 14')
        self.passEnt = Entry(self.master)
        self.passEnt.insert(0, self.password)
        self.passLab.grid(row = 2, column = 1)
        self.passEnt.grid(row = 2, column = 2)

        self.chngBtn = Button(self.master, text = 'Change', width = 20, bg = 'red', font = 'Verden 14', fg = 'white', command = self.chngOnClick)
        self.chngBtn.grid(row = 3, column = 1, columnspan = 2)

    def chngOnClick(self):
        if self.user != self.usrEnt.get() or self.password != self.passEnt.get():
            with fileinput.FileInput('regDB.txt', inplace=True, backup = '.bak') as file:
                for line in file:
                    print(line.replace(self.user, self.usrEnt.get()), end='')

            with fileinput.FileInput('regDB.txt', inplace=True, backup = '.bak') as file:
                for line in file:
                    print(line.replace(self.password, self.passEnt.get()), end='')

            with fileinput.FileInput('book.txt', inplace=True, backup = '.bak') as file:
                for line in file:
                    print(line.replace(self.user, self.usrEnt.get()), end='')
        else:
            messagebox.showwarning('Warning', 'Previous and current usernames or passwords are the same')

