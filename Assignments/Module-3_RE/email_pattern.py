import re

email="sanket_1002@gmail.com"

email_pattern="^[a-z0-9_]+[@]+[a-z]+[\.]+[a-z]"

x=re.findall(email_pattern,email)

if x:
    print("Valid Email Address!")
else:
    print("Error!Invalid Email...")


