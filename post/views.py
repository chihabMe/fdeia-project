from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from accounts.models import Profile 
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
 
@login_required
def post_like_add(request):
    data = {}
    data['success']=False
    if request.method=='POST':
        post_id = request.POST.get('post_id')

        post = Post.objects.get(id=post_id)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            data['operation']='removeing'
        else:
            post.likes.add(request.user)
            data['operation']='adding'
        data['count']=post.likes.all().count()
        data['success']=True
    return JsonResponse(data)




@login_required

def post_details(request,slug):
    context = {}
    return render(request,'post/details.html',context)

@login_required

def home (request):
    follwed_users = request.user.profile.following.all()
    obj=[]
    for user in follwed_users:
         for post in user.posts.all():
            if request.user in post.likes.all():
                 post.liked = True 
            else:
                post.liked=False
            obj.append(post)
    print(obj)
    context  = {
        'search':False,
        'posts':obj

    }
    return render (request,'post/home.html',context)
@login_required

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