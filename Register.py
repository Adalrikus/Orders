from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Register:
#usrLab  - Label for “login”
#usrEnt  - Entry for username
#passLab  - Label for “password”
#passEnt - Entry for password
#secLab - Label for “Secret word”
#secEnt - Entry for secret word
#regBtn - Button that activates “regOnClick” method
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Register')

        self.usrLab = Label(self.master, text = "Username", bg = 'white', font = 'Verden 14')
        self.usrEnt = Entry(self.master)
        self.usrLab.grid(row = 1, column = 1)
        self.usrEnt.grid(row = 1, column = 3)

        self.passLab = Label(self.master, text = "Password", bg = 'white', font = 'Verden 14')
        self.passEnt = Entry(self.master)
        self.passLab.grid(row = 2, column = 1)
        self.passEnt.grid(row = 2, column = 3)

        self.secLab = Label(self.master, text = "Secret word", bg = 'white', font = 'Verden 14')
        self.secEnt = Entry(self.master)
        self.secLab.grid(row = 3, column = 1)
        self.secEnt.grid(row = 3, column = 3)

        self.regBtn = Button(self.master, text = "Register", width = 20, bg = 'green', font = 'Verden 14', fg = 'white', command = self.regOnClick)
        self.regBtn.grid(row = 4, column = 1, columnspan = 3)

#algorithm that tries to find out the same username
#logPass - variable that stores all account information
#login - variable that copies data from logEnt
#password - variable that copies data from passEnt
#secret - variable that copies data from secEnt
    def exist(self):
        file = open('regDB.txt', 'r')
        logPass = file.read()

        login = self.usrEnt.get()
        password = self.passEnt.get()
        secret = self.secEnt.get()

        for i in range(len(logPass)):
            if logPass[i:i+4] == 'Name:':
                i += 4
                continue
            else:
                if logPass[i:i+len(login)] == login or self.secretCheck(logPass, secret):
                    return True

                if logPass[i:i+len(login)] != login:
                    while logPass[i] != '\n':
                        i += 1

                if i == len(logPass):
                    return False

#algorithm to check if the same secret word exist for another account
#secret - variable that copies data from secEnt
#logPass - variable that stores all account information
    def secretCheck(self, logPass, secret):
        for i in range(len(logPass)):
            if logPass[i:i+7] == 'Secret:':
                i += 7
                continue

            elif logPass[i:i+len(secret)] == secret:
                return True

            elif i == len(logPass):
                return False

#Registrate new user on button click
#login - variable that copies data from logEnt
#password - variable that copies data from passEnt
#secret - variable that copies data from secEnt
    def regOnClick(self):
        self.login = self.usrEnt.get()
        self.password = self.passEnt.get()
        self.secret = self.secEnt.get()

        if not self.exist():
            if self.secret is not '':
                file = open('regDB.txt', 'a')
                file.write('Name: ' + self.login + ' Password: ' + self.password + ' Secret: ' + self.secret + '\n')
    else:
        messagebox.showwarning('Warning', ‘Please, enter a secret word')
        else:
            messagebox.showwarning('Warning', 'This login already exists')

