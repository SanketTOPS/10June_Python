x=open("temp.txt","w")

id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

"""x.write(id)
x.write(name)
x.write(city)"""

x.write(f"ID:{id}")
x.write(f"\nName:{name}")
x.write(f"\nCity:{city}")