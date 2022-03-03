from django.urls import path
from psutil import virtual_memory 
from . import views

app_name = 'post'


urlpatterns = [ 
    path('',views.home,name='home')
]