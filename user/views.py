from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        
        messages.error(request,"Please enter Valid username and password.")
        return redirect('login')
    else:
        return render(request, 'user/login.html')


def userRegister(request):

    if request.method == 'GET':

        return render(request,'user/signup.html')

    else:

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Please enter Same password")
            return redirect('register')
        elif User.objects.filter(username__iexact = username):
            messages.error(request, "Username already exists.")
            return redirect('register')
        else:
            user= User.objects.create(username= username)
            user.set_password(password1)
            user.save()
            messages.success(request, "User Created Successfully.")
            return redirect('login')


@login_required
def changepassword(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            request.user.set_password(password1)
            request.user.save()
            messages.success(request, "Password Changed Successfully.")
            return redirect('login')
        else:
            messages.error(request, "Please Enter Same Password.")
            return redirect('change-password')
    else:
        return render(request, 'user/changepassword.html')

@login_required
def userLogout(request):
    logout(request)
    
    return redirect('login')
