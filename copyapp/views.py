from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'html/index.html')

def login(request):
    return render(request, 'html/login.html')

def register(request):
    return render(request, 'html/register.html')
