from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from myapp.models import *
import datetime

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

def approve_notes(request,id):
    notes=get_object_or_404(NotesData,id=id)
    notes.status="Approve"
    notes.updated_at=datetime.datetime.now()
    notes.save()
    
    #Email Sending Code
    
    return redirect('notesdata')
    
def reject_notes(request,id):
    notes=get_object_or_404(NotesData,id=id)
    notes.status="Rejected"
    notes.updated_at=datetime.datetime.now()
    notes.save()
    return redirect('notesdata')
    