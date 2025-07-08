class sanket:
    sid:int
    ssub:str

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.ssub=input("Enter Sanket's Subject:")

class ashok(sanket):
    aid:int
    asub:str

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class gopal(ashok):
    gid=0
    gsub=""

    def g_getdata(self):
        self.gid=input("Enter Gopal's ID:")
        self.gsub=input("Enter Gopal's Subject:")

class tops(gopal):
    def printdata(self):
        print("------Sanket's Info------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)
        print("------Ashok's Info------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("------Gopal's Info------")
        print("Gopal's ID:",self.gid)
        print("Gopal's Subject:",self.gsub)
    

tp=tops()
tp.s_getdata()
tp.a_getdata()
tp.g_getdata()
tp.printdata()

