import re
from sqlite3 import connect
from django.forms import ValidationError
from django.shortcuts import render
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from post.models import Post
from post.forms import PostCreate
# Create your views here.
def profile_page(request,username=None):
    if username:
        user = User.objects.get(username=username)

    else:
        user=request.user
    posts = Post.objects.filter(user=user)
    if  posts.count()==0:
        posts = None 
    if user == request.user :
        my_form = PostCreate( request.POST or None)
    else:
        my_form = None
    if request.method=='POST':
        if my_form.is_valid:
            post = my_form.save(commit=False)
            
            post.title = post.body[0:10]
            post.user = request.user
            post.save()

            
            return redirect(reverse("accounts:profile",args={username:request.user.username})) 
    context = {
        "user":user,
        'posts':posts,
        'form':my_form
    }
    return render(request,'accounts/profile.html',context)
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

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse("accounts:login"))

def registration_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("accounts:logout"))
    my_form = RegistrationForm(request.POST or None )
    if request.method=="POST":
        if my_form.is_valid():
            user  = my_form.save(commit=False)
            #do something 
            # 
            user.save()
            return redirect(reverse("accounts:login"))
    context = {
        'form':my_form
    }
    return render(request,'accounts/registration.html',context) 


    

