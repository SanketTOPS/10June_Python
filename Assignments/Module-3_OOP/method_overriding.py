class stdata:
    def getdata(self,id,name): #original
        print("ID:",id)
        print("Name:",name)

class a(stdata):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)

class b(stdata):
    def getdata(self, id, name):
        return super().getdata(id, name)
    

a1=a()
a1.getdata(101,'Sanket')

b1=b()
b1.getdata(102,'Ashok')