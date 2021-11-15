from tkinter import *
from tkinter import messagebox
import tkinter as tk
from time import *
from CheckData import *
import sqlite3

#program executing function
def execute():
    CheckData("Orders.sql")
    window = tk.Tk()
    app = Main(window)
    window.mainloop()

#fetching information from a table
def fetch(cursor, element, table, param, find):
    cursor.execute("SELECT " + element +" FROM "+ table +" WHERE "+ param +"='{0}'".format(find))
    fet = cursor.fetchone()
    if fet is not None:
        return fet[0]
    else:
        print("ERROR")
        return None


#radVar - Variable for radio button
#rd1Btn - First radio button for Customer ID
#rd2Btn - Second radio button for New Customer(generates new ID)
#cusLab - Label for "Customer ID"
#cusEnt - Customer Entry
#newLab - Label "New Customer"
#namLab - Label "Name"
#namEnt - Entry for Name
#phnLab - Label "Phone"
#phnEnt - Entry for Phone
#strLab - Label "Street"
#strEnt - Entry for Street
#hseLab - Label "House"
#hseEnt - Entry for House
#fodVar - Variable for Food
#fodLab - Label "Food"
#fodOpM - Option Menu for Food
#quaLab - Label "Quantity"
#quaEnt - Entry for Quantity
#datLab - Label "Date"
#datEnt - Entry for Date
#timLab - Label "Time"
#timEnt - Entry for Time

#Main window
class Main:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Burger Square')

        self.radVar = IntVar()

        self.rd1Btn = Radiobutton(master, text="", variable = self.radVar, value=1)
        self.rd2Btn = Radiobutton(master, text="", variable = self.radVar, value=2)
        
        self.cusLab = Label(self.master, text = 'Customer ID', bg = 'white', font = 'Verden 14')
        self.cusEnt = Entry(self.master)
        self.rd1Btn.grid(row = 1, column = 0)
        self.cusLab.grid(row = 1, column = 1)
        self.cusEnt.grid(row = 1, column = 2)

        self.newLab = Label(self.master, text = 'New Customer', bg = 'white', font = 'Verden 14')
        self.rd2Btn.grid(row = 2, column = 0)
        self.newLab.grid(row = 2, column = 1)

        self.namLab = Label(self.master, text = 'Name', bg = 'white', font = 'Verden 14')
        self.namEnt = Entry(self.master)
        self.namLab.grid(row = 3, column = 1)
        self.namEnt.grid(row = 3, column = 2)

        self.phnLab = Label(self.master, text = 'Phone', bg = 'white', font = 'Verden 14')
        self.phnEnt = Entry(self.master)
        self.phnLab.grid(row = 4, column = 1)
        self.phnEnt.grid(row = 4, column = 2)

        self.strLab = Label(self.master, text = 'Street', bg = 'white', font = 'Verden 14')
        self.strEnt = Entry(self.master)
        self.strLab.grid(row = 5, column = 1)
        self.strEnt.grid(row = 5, column = 2)

        self.hseLab = Label(self.master, text = 'House', bg = 'white', font = 'Verden 14')
        self.hseEnt = Entry(self.master)
        self.hseLab.grid(row = 6, column = 1)
        self.hseEnt.grid(row = 6, column = 2)

        self.fodVar = StringVar(self.master)
        self.fodVar.set('Burger Classic')
        self.fodLab = Label(self.master, text = 'Food', bg = 'white', font = 'Verden 14')
        self.fodOpM = OptionMenu(master, self.fodVar, "Burger Classic", "Burger Extra Big", "Burger Extra Dip", "Burger #9")
        self.fodOpM.configure(background = 'white')
        self.fodLab.grid(row = 7, column = 1)
        self.fodOpM.grid(row = 7, column = 2)

        self.quaLab = Label(self.master, text = 'Quantity', bg = 'white', font = 'Verden 14')
        self.quaEnt = Entry(self.master)
        self.quaLab.grid(row = 8, column = 1)
        self.quaEnt.grid(row = 8, column = 2)

        self.datLab = Label(self.master, text = 'Date', bg = 'white', font = 'Verden 14')
        self.datEnt = Entry(self.master)
        self.datLab.grid(row = 9, column = 1)
        self.datEnt.grid(row = 9, column = 2)

        self.timLab = Label(self.master, text = 'Time', bg = 'white', font = 'Verden 14')
        self.timEnt = Entry(self.master)
        self.timLab.grid(row = 10, column = 1)
        self.timEnt.grid(row = 10, column = 2)

        self.prcBtn = Button(self.master, text = 'Price', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command=lambda: self.PriceDisplay(self.fodVar.get(), self.quaEnt.get()))
        self.prcBtn.grid(row = 11, column = 0, columnspan = 3)

        self.savBtn = Button(self.master, text = 'Save', width = 20, bg = 'green', font = 'Verden 14', fg = 'white', command=lambda: self.SaveData(self.radVar.get(), self.namEnt.get(), self.phnEnt.get(), self.strEnt.get(), self.hseEnt.get(), self.fodVar.get(), self.quaEnt.get(), self.datEnt.get(), self.timEnt.get())
)
        self.savBtn.grid(row = 12, column = 0, columnspan = 3)

        self.clsBtn = Button(self.master, text = 'Close', width = 20, bg = 'red', font = 'Verden 14', fg = 'white', command=self.Close)
        self.clsBtn.grid(row = 13, column = 0, columnspan = 3)

#price displaying function
    def PriceDisplay(self, food, quantity):
        #converting string to integer
        quantity = [int(x) for x in quantity.split() if x.isdecimal()]
        if len(quantity) is not 0:
            quantity = quantity[0]
        #connecting to database
        dataBase = sqlite3.connect("Orders.sql")
        cursor   = dataBase.cursor()
        cursor.execute("SELECT food_price FROM foods WHERE food_name='{0}'".format(food))
        #checking database
        fet = cursor.fetchone()
        if fet is not None:
            price  = int(fet[0])
            price *= quantity
        else:
            print("ERROR")
        #displaying price
        messagebox.showinfo("Price", food + " x " + str(quantity) + " = " + str(price))

#window closing function
    def Close(self):
        self.master.destroy()


#data saving function
    def SaveData(self, rdBtn, cname, cphone, cstreet, chouse, cfood, cquantity, cdate, ctime):
        #connecting to the database
        dataBase = sqlite3.connect("Orders.sql")
        cursor   = dataBase.cursor()
        #checking inputs
        if len(cdate) is not 0 and len(ctime) is not 0:
            cdate = strptime(cdate, "%d %m %y")
            cdate = strftime("%a, %d %b %Y", cdate)
            ctime = strptime(ctime, "%H %M %S")
            ctime = strftime("%H:%M:%S", ctime)
            print(cdate + " " + ctime)
        else:
            cdate = strftime("%a, %d %b %Y", localtime())
            ctime = strftime("%H:%M:%S", localtime())
            print(cdate + " " + ctime)
        #calculating price of an order
        price = fetch(cursor, "food_price", "foods", "food_name", cfood) * float(cquantity)
        #getting food's name
        cfood = fetch(cursor, "food_id", "foods", "food_name", cfood)
        #checking ID and inserting information to database
        if rdBtn is 1 and self.cusEnt.get() is not None:
            rdBtn = int(self.cusEnt.get())
            customer_info = (rdBtn, cname, cphone, cstreet, chouse)
            cursor.execute("INSERT INTO customer(customer_id, name, phone_no, street, house) VALUES(?, ?, ?, ?, ?);", customer_info)
            dataBase.commit()

            orders_info = (cdate, ctime, cquantity, rdBtn, cfood, price)
            cursor.execute("INSERT INTO orders(date, time, quantity, customer_id, food_id, total_price) VALUES(?, ?, ?, ?, ?, ?);", orders_info)
            dataBase.commit()
        elif rdBtn is 2:
            customer_info = (cname, cphone, cstreet, chouse)
            cursor.execute("INSERT INTO customer(name, phone_no, street, house) VALUES(?, ?, ?, ?);", customer_info)
            dataBase.commit()

            customer_id = fetch(cursor, "customer_id", "customer", "name", cname)
            orders_info = (cdate, ctime, cquantity, customer_id, cfood, price)
            cursor.execute("INSERT INTO orders(date, time, quantity, customer_id, food_id, total_price) VALUES(?, ?, ?, ?, ?, ?);", orders_info)
            dataBase.commit()
#error messages
        elif rdBtn is None:
            messagebox.showerror("Customer ID", "You didn't press radio button")
            return False
        elif self.cusEnt.get() is None:
            messagebox.showerror("Customer ID", "You didn't enter your ID")
            return False
        else:
            messagebox.showerror("Customer ID", "Please, choose one of the option")
            return False


execute()
