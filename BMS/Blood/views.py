from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'Blood/home.html')

def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        aduser=authenticate(username=username,password=password)
        if aduser:
            login(request,aduser)
            return HttpResponseRedirect(reverse('Blood:adminpanel'))
            # if docuser.is_active:
            #     login(request,docuser)
            #     return HttpResponseRedirect(reverse('docpanel'))
            # else:
            #     return HttpResponse("Account not active")
        else:
            print("A login failed")
            return(HttpResponse("Invalid login details!"))
    else:
        return render(request,'Blood/adminlogin.html',{})

def adminpanel(request):
    return render(request,'Blood/adminpanel.html')

def adminpaneldoctor(request):
    return render(request,'Blood/adminpaneldoctor.html')

def adminpaneldonations(request):
    return render(request,'Blood/adminpaneldonations.html')

def adminpaneldonors(request):
    return render(request,'Blood/adminpaneldonors.html')

def adminpanelpatients(request):
    return render(request,'Blood/adminpanelpatients.html')

def adminpanelrequests(request):
    return render(request,'Blood/adminpanelrequests.html')