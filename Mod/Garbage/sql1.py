import sqlite3

db = sqlite3.connect("Orders.sql")
cursor = db.cursor()

cursor.execute('''
        SELECT * FROM customer;
        ''')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
        SELECT * FROM orders;
        ''')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
