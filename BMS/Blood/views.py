from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'Blood/home.html')

# def adminlogin(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         aduser=authenticate(username=username,password=password)
#         if aduser:
#             if aduser.is_active and aduser.is_superuser:
#                 login(request,aduser)
#                 return HttpResponseRedirect(reverse('Blood:adminpanel'))
#             else:
#                 return HttpResponse("Account not active")
#         else:
#             print("A login failed")
#             return(HttpResponse("Invalid login details!"))
#     else:
#         return render(request,'Blood/adminlogin.html',{})

@login_required
def adminlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpanel(request):
    return render(request,'Blood/adminpanel.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpaneldoctor(request):
    return render(request,'Blood/adminpaneldoctor.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpaneldonations(request):
    return render(request,'Blood/adminpaneldonations.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpaneldonors(request):
    return render(request,'Blood/adminpaneldonors.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpanelpatients(request):
    return render(request,'Blood/adminpanelpatients.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpanelrequests(request):
    return render(request,'Blood/adminpanelrequests.html')