from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
#Login
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid details")
            return redirect('login')
    return render(request,"login.html")
# Logout
def logout(request):
    auth.logout(request)
    return redirect('/')

#Registration
def register(request):
    if request.method=='POST':
        username=request.POST['Username']
        first_name=request.POST['First_name']
        last_name=request.POST['Last_name']
        email=request.POST['email']
        password=request.POST['Password']
        cpassword=request.POST['Password1']
        if password==cpassword :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"Password doesn't match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")