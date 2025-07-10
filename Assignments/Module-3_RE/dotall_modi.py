import re

mystr="That is Python!"

#x=re.findall("Py...on",mystr)
x=re.findall("This|These",mystr)
print(x)
