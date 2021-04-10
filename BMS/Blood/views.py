from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Blood/home.html')

def adminlogin(request):
    return render(request,'Blood/adminlogin.html')