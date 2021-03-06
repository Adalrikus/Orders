import sqlite3
import os.path

#Database checking class
class CheckData:
    def __init__(self, dbName):
        currentPath = os.getcwd()
        dataBase    = sqlite3.connect(currentPath + "/" + dbName)
        cursor      = dataBase.cursor()
        cursor.execute('''
            SELECT name FROM sqlite_master WHERE type='table';
            ''')

        #checking size of a database
        if len(cursor.fetchall()) is 0:
            print("Database is empty\nCreating database")
            self.CreateTables(dataBase)
            print("Database created")
        else:
            print("Database [x]")

        #checking each table
        checkCustomerTable = self.CheckTableExists(dataBase, "customer")
        checkFoodsTable    = self.CheckTableExists(dataBase, "foods")
        checkOrdersTable   = self.CheckTableExists(dataBase, "orders")


        if checkCustomerTable and checkFoodsTable and checkOrdersTable:
            print("Tables   [x]")
        else:
            print("Database is damaged\nRestoring sequence activated")
            os.remove("Orders.sql")
            dataBase = sqlite3.connect("Orders.sql")
            cursor   = dataBase.cursor()
            self.CreateTables(dataBase)
            print("Database restored")
            cursor.close()
        
        cursor.close()

    #database creating function
    def CreateTables(self, dbcon):
        cursor = dbcon.cursor()
        cursor.executescript('''
            CREATE TABLE customer(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT,
            phone_no    TEXT,
            street      TEXT,
            house       TEXT
            );

            CREATE TABLE foods(
            food_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name   TEXT,
            food_price  REAL
            );

            CREATE TABLE orders(
            order_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            date        TEXT,
            time        TEXT,
            quantity    INTEGER,
            customer_id INTEGER,
            food_id     INTEGER,
            total_price REAL,
            FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
            FOREIGN KEY(food_id) REFERENCES foods(food_id)
            );

            INSERT INTO foods(food_name, food_price)
            VALUES('Burger Classic', 1000);
            INSERT INTO foods(food_name, food_price)
            VALUES('Burger Extra Big', 1500);
            INSERT INTO foods(food_name, food_price)
            VALUES('Burger Extra Dip', 2000);
            INSERT INTO foods(food_name, food_price)
            VALUES('Burger #9', 2500);
        ''')

    #table existence checking function
    def CheckTableExists(self, dbcon, tablename):
        cursor = dbcon.cursor()
        cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type='table' AND name='{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if cursor.fetchone()[0] == tablename:
            cursor.close()
            return True

        cursor.close()
        return False

