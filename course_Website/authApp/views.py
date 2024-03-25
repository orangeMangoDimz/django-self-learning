from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def loginView(request):
    
    if request.user.is_authenticated:
            return redirect('main:home')
    
    template_name = 'auth/login.html'
    
    if request.method == "POST":
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')
        user_auth = authenticate(request, username = user_username, password = user_password)
        
        if user_auth is not None:
            login(request, user_auth)
            return redirect('main:home')
        else: 
            messages.error(request, "Invalid username or password!")
    
    return render(request, template_name)
    
def register(request):
    tempalte_name = 'auth/register.html'
    return render(request, tempalte_name)

@login_required
def logoutView(request):
    logout(request)
    return redirect('main:home')