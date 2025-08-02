from django.shortcuts import render
import random

# Create your views here.
def index(request):
    name="Nirav"
    return render(request,'index.html',{'name':name})

num=1
def new(request):
    #num=random.randint(1111,9999)
    global num
    num+=1
    if num==10:
        num=1
    return render(request,'new.html',{'num':num})