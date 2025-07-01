x=open("stdata.txt","a")

n=int(input("Enter number of students! : "))


if x.writable():

    for i in range(n):
        id=input("Enter an ID:")
        name=input("Enter a Name:")
        city=input("Enter a City:")

        x.write(f"\nID:{id}\nName:{name}\nCity:{city}\n")