from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    
    email = models.EmailField(unique=True, blank=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=GENDER_MALE, null=True, blank=True)
    profile_picture=models.ImageField(upload_to='images/', default='default-pp.png', null=True, blank=True)
    

