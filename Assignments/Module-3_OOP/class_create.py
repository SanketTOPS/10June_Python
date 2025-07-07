class student:
    stid=101
    stnm="Sanket"

    def getdata(self):
        print("This is Student class!")


st=student() #object of class

print("ID:",st.stid)
print("Name:",st.stnm)

st.getdata()

