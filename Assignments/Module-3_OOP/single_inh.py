class father:
    bal:int
    car:int

    def getdata(self):
        self.bal=input("Enter a bank balance:")
        self.car=input("Enter a car details:")

class son(father):
    def printdata(self):
        print("Total Balance:",self.bal)
        print("Total Car:",self.car)


sn=son()
sn.getdata()
sn.printdata()