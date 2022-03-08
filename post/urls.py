
from unicodedata import name
from django.urls import path

from . import views

app_name = 'post'


urlpatterns = [ 
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('<slug:slug>/',views.post_details,name='post-details'),
    path('post/post-like',views.post_like_add),

]
