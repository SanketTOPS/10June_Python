from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def admin_login(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        
        if unm=='tops' and pas=='tops@123':
            print("Login Successfull!")
            return redirect('admin-dashboard')
        else:
            print("Error!Login Faild....")
    return render(request,'admin_login.html')

def admin_dashboard(request):
    data=UserSignup.objects.all()
    x=data.count()
    return render(request,'admin_dashboard.html',{'x':x})

def userdata(request):
    data=UserSignup.objects.all()
    return render(request,'userdata.html',{'data':data})

def notesdata(request):
    ndata=NotesData.objects.all()
    return render(request,'notesdata.html',{'ndata':ndata})