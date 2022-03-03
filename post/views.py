from django.shortcuts import render

# Create your views here.
def home (request):
    context  = {}
    return render (request,'post/home.html',context)