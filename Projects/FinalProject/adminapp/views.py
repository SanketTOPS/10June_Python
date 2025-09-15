from django.shortcuts import render,redirect

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
    return render(request,'admin_dashboard.html')

def userdata(request):
    return render(request,'userdata.html')