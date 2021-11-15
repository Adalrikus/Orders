import os.path
from tkinter import *
from Settings import *
import tkinter as tk

class Main:
#user - variable for username
#password - password for account
#btnSet - Button that creates new Settings window 
#trnN - variable that store train’s number
#trnNLab - Label for “Train #”
#trnNOpM - option menu
#frmEnt - entry for current location of user
#frmLab - Label for “From:”
#toEnt - entry for final destination of user
#toLab - Label for “To:”
#subBtn - Button that activates “subOnClick” method
    def __init__(self, master, user, password):
        self.master = master
        self.user = user
        self.password = password
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Railway booking system')

        self.btnSet = Button(self.master, text = 'Settings', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.setOnClick)
        self.btnSet.grid(row = 1, column = 1)

        self.trnN = IntVar()
        self.trnN.set(1)

        self.trnNLab = Label(self.master, text = 'Train #', bg = 'white', font = 'Verden 14')
        self.trnNOpM = OptionMenu(self.master, self.trnN, 1, 2, 3, 4, 5)
        self.trnNOpM.configure(background = 'white')
        self.trnNLab.grid(row = 1, column = 2)
        self.trnNOpM.grid(row = 1, column = 3)

        self.frmLab = Label(self.master, text = 'From: ', bg = 'white', font = 'Verden 14')
        self.frmEnt = Entry(self.master)
        self.frmLab.grid(row = 2, column = 2)
        self.frmEnt.grid(row = 2, column = 3)

        self.toLab = Label(self.master, text = 'To: ', bg = 'white', font = 'Verden 14')
        self.toEnt = Entry(self.master)
        self.toLab.grid(row = 3, column = 2)
        self.toEnt.grid(row = 3, column = 3)

        self.subBtn = Button(self.master, text = 'Submit', width = 20, bg = 'red', font = 'Verden 14', fg = 'white', command = self.subOnClick)
        self.subBtn.grid(row = 4, column = 2, columnspan = 2)

#Opens new window with Settings form
#newWindow - priority to new window
#app - creating new window
    def setOnClick(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Settings(self.newWindow, self.user, self.password)

#Collects data from entries and option menu and saves it in “book.txt”
    def subOnClick(self):
        fileName = 'book.txt'
        if os.path.isfile(fileName): #checks existence of file
            file = open(fileName, 'a')
            if self.notRepInBook():
                file.write('User: ' + self.user + ' Train #: ' + str(self.trnN.get()) + ' From: ' + self.frmEnt.get() + ' To: ' + self.toEnt.get() + '\n') #saves data in file
            else:
                messagebox.showwarning('Warning', 'You\'ve already booked this destination')
        else:
            file = open(fileName, 'w') #creates file
            file.write('User: ' + self.user + ' Train #: ' + self.trnN.get() + ' From: ' + self.frmEnt.get() + ' To: ' + self.toEnt.get() + '\n')

#checks iterance of data
    def notRepInBook(self):
        file = open('book.txt', 'r')
        user = file.read()

        for i in range(len(user) + 1):
            if user[i:i+len(self.user)] == self.user:
                while user[i-6:i] != 'From: ':
                    i += 1

                if user[i:i+len(self.frmEnt.get())] == self.frmEnt.get():
                    while user[i-4:i] != 'To: ':
                        i += 1

                    if user[i:i+len(self.toEnt.get())] == self.toEnt.get():
                        return False
                    else:
                        continue
                else:
                    continue
            if i == len(user):
                return True

