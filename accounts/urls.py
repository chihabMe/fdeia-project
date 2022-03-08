from django.urls import path 
from . import views 
app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_page,name ='login'),
    path('signup/',views.registration_page,name='register'),
    path('logout/',views.logout_page,name ='logout'),
    path('<slug:username>/profile',views.profile_page,name ='profile'),
    path('user-like',views.user_like),
    path('user-follow',views.user_follow),
    path('user-profile-image-change',views.user_profile_image_change),
    path('user-profile-boi-change',views.user_profile_boi_change),
]