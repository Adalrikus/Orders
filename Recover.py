from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Recovery:
#New window named Recovery
#logRecBtn - Button which creates new button, label and entry and destroy itself
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Recovery')

        self.logRecBtn = Button(self.master, text = 'Recover', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.logOnClick)
        self.logRecBtn.grid(row = 1, column = 1)

#logRecBtn - Button which creates new button, label and entry and destroy itself
#secLab - Label for “Secret word”
#secEnt - Entry for secret word
#recBtn - button which triggers “logRecOnClick” method
    def logOnClick(self):
        self.logRecBtn.destroy()

        self.logRecLab = Label(self.master, text = 'Recover login', bg = 'white', font = 'Verden 14')
        self.logRecLab.grid(row = 1, column = 1, columnspan = 2)

        self.secLab = Label(self.master, text = 'Enter your secret word', bg = 'white', font = 'Verden 14')
        self.secEnt = Entry(self.master)
        self.secLab.grid(row = 2, column = 1)
        self.secEnt.grid(row = 2, column = 2)

        self.recBtn = Button(self.master, text = 'Recover', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.logRecOnClick)
        self.recBtn.grid(row = 3, column = 1, columnspan = 2)

#algorithm that aims to find out account information with the same secret word
#secret - variable that copies data from secEnt
#st - beginning of an array
#end - end of an array
#login - variable that will store all information about account
#secList - array that stores all data from “regDB.txt” file
    def logRecOnClick(self):
        secret = self.secEnt.get()
        st = 0
        end = 0
        login = ''

        file = open('regDB.txt', 'r')
        secList = file.read()

        for i in range(len(secList)):
            if secList[i:i+7] == 'Secret:':
                i += 7
                continue
            else:
                if secList[i:i+len(secret)] == secret:
                    j = i + len(secret)
                    while secList[i:i+5] != 'Name:':
                        i -= 1
                        st = i

                    end = j

                    login = secList[st:end]
                    messagebox.showinfo('Login', login)

                if secList[i:i+len(secret)] != secret:
                    continue

                if i == len(secList):
                    messagebox.showerror('Not found', 'Can\'t find same secret word')

