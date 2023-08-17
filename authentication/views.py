from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def authlogin(request):
    if request.method == 'POST':
        get_username = request.POST['username']
        get_password = request.POST['password']
        user = authenticate(request, username=get_username, password=get_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('profile_new')
        else:
            messages.error(request, 'Email or password was invalid!')

    return render(request, 'authentication/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('login')

def authregister(request):
    if request.method == 'POST':
        get_username = request.POST['username']
        get_email = request.POST['email']
        get_password = request.POST['password']
        get_confirm_password = request.POST['confirm_password']
        if get_password == get_confirm_password:
            if User.objects.filter(username=get_username).exists():
                messages.error(request, 'Username already exists!')

            elif User.objects.filter(email=get_email).exists():
                messages.error(request, 'Email already exists!')

            else:
                register_user = User.objects.create_user(username = get_username, email=get_email, password=get_password)
                register_user.save()
                messages.success(request, 'Registration successfully!')
                return redirect('profile_new')
        else:
            messages.error(request, 'Password or Confirm Password not matchied!')

    return render(request, 'authentication/register.html')


def forgetpassword(request):
    return render(request, 'authentication/forget.html')


