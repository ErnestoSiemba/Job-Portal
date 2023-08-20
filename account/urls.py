from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    
]
