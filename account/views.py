from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm, UserLoginForm



@login_required
def home(request):
    return render(request, 'account/home.html')

def registerUser(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # username = form.cleaned_data['username']
                return redirect('login')
            else:
                return redirect('register')
        else: 
            form = CreateUserForm()
        return render(request, 'account/register.html', {'form': form})
    else:
        return redirect('logout')


def loginUser(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error('Invalid username or password')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
                
        form = UserLoginForm()
        return render(request, 'account/login.html', {'form': form})
    else:
        return redirect('home')

def profile(request):
    return render(request, 'account/profile.html')
