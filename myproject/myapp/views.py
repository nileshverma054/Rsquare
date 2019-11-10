from django.shortcuts import render, redirect
from myapp.models import users
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/index.html')

def signup(request):
    return render(request, 'myapp/signup.html')    

def login(request):
    return render(request, 'myapp/login.html')    

def dashboard(request):
    return render(request, 'myapp/dashboard.html')    
