def getdata(id,name):
    return id,name

def userinfo():
    x=getdata(101,'Sanket')
    print("ID:",x[0])
    print("Name:",x[1])

userinfo()