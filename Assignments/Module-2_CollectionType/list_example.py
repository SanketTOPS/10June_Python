tech=['python','php','java','react','ruby']
"""print(tech)

print(tech[0])
print(tech[-1])
print(tech[0:3]) #range
print(tech[2:])
print(tech[:3])"""

# --------------------------- #
#print(tech)
#tech[1]='html' #change the value
#print(len(tech))
#print(tech)

"""if 'JAVA' in tech:
    print("Yes...")
else:
    print("Noo")"""

"""for i in tech:
    print(i)"""

"""print(tech)
print(tech.index('react'))"""

"""for i in tech:
    print(f"{i}={tech.index(i)}")"""


# ---------------------- #
print(tech)
#tech.append("angular")
#tech.insert(2,"css")
#tech.remove('java')
#tech.pop()
#tech.pop(0)
#del tech[1]
#tech.clear()
#del tech
#tech.reverse()
#tech.sort()
#tech.sort(reverse=True)
#print(tech)

#newtech=tech.copy()
#print(newtech)

newtech=["c","c++","ds","sql"]
print(newtech)

print(tech+newtech)
tech.extend(newtech)
print(tech)

