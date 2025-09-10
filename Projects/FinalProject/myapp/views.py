from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def notes(request):
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

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
    