import re

mystr="That is Python!21211"

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B211',mystr)
#x=re.findall('\AThat',mystr)
#x=re.findall('211\Z',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
x=re.findall('\S',mystr)
print(x)