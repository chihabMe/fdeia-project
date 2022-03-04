from unicodedata import name
from django.urls import path
from psutil import virtual_memory 
from . import views

app_name = 'post'


urlpatterns = [ 
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('<slug:slug>/',views.post_details,name='post-details')
]