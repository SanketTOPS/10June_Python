def getdata(data):
    print("ID:",data['id'])
    print("Name:",data['nm'])
    print("Sub:",data['sub'])
    print("City:",data['ct'])

#getdata({'id':101,'nm':'Sanket','sub':'Python','ct':'Rajkot'}) #Dict. argu.


stid=input("Enter an ID:")
stnm=input("Enter a Name:")
stsub=input("Enter a Subject:")
stct=input("Enter a City:")

getdata({'id':stid,'nm':stnm,'sub':stsub,'ct':stct})