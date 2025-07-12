import re

username="Sanket2020"

x=re.findall('[A-Z]+[a-z]+[0-9]',username)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username...")