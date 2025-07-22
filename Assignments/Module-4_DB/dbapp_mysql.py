import pymysql

try:
    dbcon=pymysql.connect(host="localhost",user="root",password="",database="topsdb")
    print("Database connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()

#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','bhavnagar'),('hitesh','morbi'),('mahesh','baroda'),('mitesh','ahmedabad')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)
"""

#Update Data
"""update_data="update studinfo set name='hardik', city='navsari' where id=4"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

#Delet Data
"""delete_data="delete from studinfo where id=4"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""

#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i)

except Exception as e:
    print(e)