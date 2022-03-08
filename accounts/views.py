import json
from sqlite3 import connect
from django.forms import ValidationError
from django.shortcuts import render
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from post.models import Post
from post.forms import PostCreate
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def user_profile_image_change(request):
    data = {}
    data['success']=False
    if request.method=="POST":
        image = request.FILES.get("image")
        profile = Profile.objects.get(user=request.user)
        profile.image=image 
        profile.save()
        data['imageUrl']=profile.image.url
        data['success']=True
    return JsonResponse(data)
def user_follow(request):
    data = {}
    if request.method=="POST":

        user_id = request.POST.get("user_id")
        user = get_object_or_404(User,id=user_id)
        if request.user in user.profile.followers.all():
            request.user.profile.following.remove(user) 
            user.profile.followers.remove(request.user)
            data['msg']='success'
            data['operation']='removing'
            data["count"]=user.profile.get_followers_count();
        else:
            request.user.profile.following.add(user) 
            user.profile.followers.add(request.user)
            data['msg']='success'
            data['operation']='adding'
            data["count"]=user.profile.get_followers_count();
        data['method']=request.method

        return JsonResponse(data)   
def user_like(request):
    data = {}

    if request.method=="POST":
        user_id = request.POST.get("user_id")
        user = get_object_or_404(User,id=user_id)
        if request.user in user.profile.likes.all():
            user.profile.likes.remove(request.user)
            data['msg']='success'
            data['operation']='removing'
        else:
            user.profile.likes.add(request.user)
            data['msg']='success'
            data['operation']='adding'
        data["count"]=user.profile.get_likes_count();
    return JsonResponse(data)
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
    liked = request.user in user.profile.likes.all()
    followed = request.user in user.profile.followers.all()
    print('-------------')
    print(liked)
    print(followed)
    print('-------------')
    context = {
        "user":user,
        'posts':posts,
        'form':my_form,
        'followed':followed,
        'liked':liked
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


    

