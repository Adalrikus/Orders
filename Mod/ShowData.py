from tkinter import *
from tkinter import ttk
import tkinter as tk
from CheckData import *
import sqlite3

#program executing function
def execute():
    CheckData("Orders.sql")
    window = tk.Tk()
    app = OrderRecords(window)
    window.mainloop()

#orders displaying window
class OrderRecords:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Order Records')
        self.master.resizable(width = 0, height = 0)
        #connecting to database
        connect = sqlite3.connect("Orders.sql")
        cursor  = connect.cursor()
        cursor.execute("SELECT * FROM orders;")
        orders  = cursor.fetchall()
        #creating treeview
        self.tree = ttk.Treeview(self.master, selectmode = 'browse')
        self.tree.pack(side = 'left', in_ = self.frame)

        self.treeYScroll = ttk.Scrollbar(self.master, orient = "vertical", command = self.tree.yview)
        self.treeYScroll.pack(side = "right", fill = "y", in_ = self.frame)
        self.tree.configure(yscrollcommand=self.treeYScroll.set)

        self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        self.tree['show'] = 'headings'

        headings = ["Order ID", "Date", "Time", "Quantity", "Customer ID", "Food ID", "Total price"]
        #inserting all data in tree
        for i in range(1, 8):
            self.tree.column(str(i), stretch = False, width = 120)
            self.tree.heading(str(i), text = headings[i-1])

        self.InsertData(orders)

        self.frame.pack()

        self.clsBtn = Button(self.master, text = "Close", command = self.master.destroy)
        self.clsBtn.pack()

#data inserting function
    def InsertData(self, orders):
        for order, i in zip(orders, range(len(orders))):
            self.tree.insert('', 'end', values = order)

execute()
