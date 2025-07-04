class student:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is member function of students class.")


#Objcet
st=student()
print("ID:",st.stid)
print("Name:",st.stnm)

st.myfunc()