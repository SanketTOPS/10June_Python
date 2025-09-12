from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from FinalProject import settings

# Create your views here.
def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def notes(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        form=NotesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Notes has been submitted!")
            msg="Notes has been submitted!"
            #return redirect('notes')
        else:
            print(form.errors)
            msg="Error!Something went wrong..."
    return render(request,'notes.html',{'user':user,'msg':msg})

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Your form has been submitted!"
            
            #Email Sending Code
            send_mail(subject="Thank You!",message="Thank you for connecting us!\nWe will contact you.\n\nEnjoy our serviece!\n\nThanks & Regards!\nSanket Chauhan\nNotesApp Team\nsanket.tops@gmail.com | +91 9724799469",from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST['email']])
            
        else:
            msg="Error!Something went wrong..."
    return render(request,'contact.html',{'user':user,'msg':msg})

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=UserSignup.objects.get(id=userid)
    if request.method=='POST':
        form=UpdateForm(request.POST,instance=cuser)
        if form.is_valid():
            form.save()
            print("Profile updated!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'profile.html',{'user':user,'userid':cuser})

def signin(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=UserSignup.objects.filter(username=unm,password=pas)
        userid=UserSignup.objects.get(username=unm)
        print("UserID:",userid.id)
        if user:
            print("Login Successfully!")
            request.session['user']=unm
            request.session['userid']=userid.id
            return redirect('/')
        else:
            print("Error!Login faild....")
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'signup.html')


def userlogout(request):
    logout(request)
    return redirect('/')
    