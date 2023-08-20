from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

class ProfileUpdateView(generic.UpdateView):
    form_class = UserProfileForm
    template_name = 'userprofile/profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    