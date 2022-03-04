from django.forms import ValidationError
from django.shortcuts import render
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

def login_page(request):
    my_form = LoginForm(request.POST or None)

    if request.method=="POST":
        if my_form.is_valid():
            username = my_form.cleaned_data.get("username")
            password= my_form.cleaned_data.get("password")
            print(username,password)
            user = authenticate(username=username,password=password)
            if user is not None:
                    login(request,user=user)
                    return redirect(reverse("post:home"))
    context = {
        "form":my_form
    }
    return render(request,'accounts/login.html',context) 

def logout(request):
    if request.is_authenticated():
        logout(request)
    return redirect(reverse("accounts:login"))

def registration_page(request):
    if request.is_authenticated():
        return redirect(reverse("accounts:logout"))
    my_form = RegistrationForm()

    
