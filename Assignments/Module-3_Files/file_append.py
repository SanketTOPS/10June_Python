x=open("temp.txt","a")

id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

x.write(f"ID:{id}")
x.write(f"\nName:{name}")
x.write(f"\nCity:{city}")