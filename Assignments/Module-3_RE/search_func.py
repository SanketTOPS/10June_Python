import re

mystr=input("Enter any string:")

x=re.search("Python",mystr)
print(x)

if x: #TRUE
    print("Match Done!")
else:
    print("Error!")
