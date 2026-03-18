from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_user,logout
from .models import Customer


def sign_out(request):
    logout(request)
    return redirect('login') 

def signup_page(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(username=username,email=email,password=password)
        Customer.objects.create(user=user)
        return redirect('login') 
    else:
        return render(request, "signup.html")
def login_page(request):
        if request.method == 'POST':
            username_value= request.POST.get('username')
            password_value=request.POST.get('password')
            user=authenticate(request,username=username_value,password=password_value)
            
            if user is not None:
                auth_user(request, user)
                return redirect('products') # SUCCESS: Redirect to products
            else:
                return redirect('signup')
            
        return render(request, "login.html")
