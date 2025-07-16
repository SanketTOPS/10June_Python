import sqlite3

try:
    con=sqlite3.connect("topsdb.db")
    print("Database Created/Connected!")
except Exception as e:
    print(e)

#Table Created
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    con.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('hitesh','surat'),('ashok','bhavnagar')"
try:
    con.execute(insert_data)
    con.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set city='jamnagar' where id=7"
try:
    con.execute(update_data)
    con.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

#Delete Data
delete_data="delete from studinfo where id=3"
try:
    con.execute(delete_data)
    con.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)