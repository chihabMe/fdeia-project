from django.shortcuts import render
from django.contrib.auth.models import User 
# Create your views here.
def post_details(request,slug):
    context = {}
    return render(request,'post/details.html',context)
def home (request):
    context  = {
        'search':False

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