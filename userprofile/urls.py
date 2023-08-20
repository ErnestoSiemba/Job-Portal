from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('profile_update/', views.ProfileUpdateView.as_view(), name='profile-update'),
]
