import re

mystr="that is Python!787895695159"

#x=re.match("^This",mystr)
#x=re.match("^[A-Z]",mystr)
x=re.findall('156$',mystr)

print(x)