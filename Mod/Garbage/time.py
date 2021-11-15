import sqlite3
import datetime as DT

def adapt_timeobj(timeobj):
    return (3600*timeobj.hour + 60*timeobj.minute + timeobj.second)

def convert_timeobj(val):
    val = int(val)
    hour, val = divmod(val, 3600*10**6)
    minute, val = divmod(val, 60*10**6)
    second, val = divmod(val, 10**6)
    return DT.time(hour, minute, second)


# Converts DT.time to TEXT when inserting
sqlite3.register_adapter(DT.time, adapt_timeobj)

# Converts TEXT to DT.time when selecting
sqlite3.register_converter("timeobj", convert_timeobj)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()

# declare timecol to be of type timeobj
cur.execute("create table test (timecol timeobj)")

cur.executemany("insert into test (timecol) values (?)", 
                [DT.time(1,2,3)] )

cur.execute("select * from test;")
rows = cur.fetchone()
for row in rows:
    print(row)
