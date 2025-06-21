stdata={'id':101,
        'name':'sanket',
        'city':'rajkot'}

"""print(stdata)
print(stdata['name'])
print(stdata.get('city'))
print(len(stdata))"""
#print(stdata.keys())
#print(stdata.values())

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


# --------------------------- #
print(stdata)
#stdata['id']=102
#stdata['sub']='Python' #add a new pair
#stdata.pop('city')
#stdata.clear()
#del stdata['name']
#del stdata
#print(stdata)


newdict=stdata.copy()
print(newdict)