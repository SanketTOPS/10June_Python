stdata={}

n=int(input("Enter number of pairs for dict.:"))

for i in range(n):
    key=input("Enter a Key:")
    value=input("Enter a Value:")
    stdata[key]=value

print(stdata)