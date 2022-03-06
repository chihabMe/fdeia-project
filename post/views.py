from django.shortcuts import render
from django.contrib.auth.models import User 
from accounts.models import Profile 
from itertools import chain
from .models import Post
# Create your views here.
def post_details(request,slug):
    context = {}
    return render(request,'post/details.html',context)
def home (request):
    follwed_users = request.user.profile.following.all()
    print(follwed_users)
    obj=[]

    for user in follwed_users:
         for post in user.posts.all():
             obj.append(post)
    print(obj)
    context  = {
        'search':False,
        'posts':obj

    }
    return render (request,'post/home.html',context)
def search (request):
    qr = request.GET.get('qr')
    context  = {}
    if qr is not None and qr!='':
        qr = User.objects.filter(username__icontains=qr)
        
        context['search']=True 
        
        if qr.exists:
            context['results']=qr
        else:
            context['results']=None
    return render (request,'post/home.html',context)