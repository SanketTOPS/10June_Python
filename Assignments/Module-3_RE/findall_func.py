import re

#mystr=input("Enter any string:")
mystr="This is Python!"

x=re.findall("is",mystr)
print(x)

if x: #TRUE
    print("Match Done!")
else:
    print("Error!")
