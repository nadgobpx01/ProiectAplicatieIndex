from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def public_home(request):
    return render(request, 'core/public_home.html')

def about(request):
    return render(request, 'core/about.html')

def home(request):
    return render(request, 'core/home.html')
