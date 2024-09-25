from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth import login
from .forms import SignupForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to a home or success page
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  # Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/mylogin.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  # Handle both form data and file (resume)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('home')  # Redirect to homepage after successful signup
    else:
        form = SignupForm()  

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('home') 
