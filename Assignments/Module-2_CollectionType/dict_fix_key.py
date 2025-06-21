stdata={}

keys=['id','name','city']

for i in range(len(keys)):
    value=input(f"Enter a value for {keys[i]}:")
    stdata[keys[i]]=value

print(stdata)