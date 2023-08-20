from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.jobs, name='jobs'),
    path('postjob/', views.postjob, name='postjob'),
]
