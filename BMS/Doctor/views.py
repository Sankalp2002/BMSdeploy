from django.shortcuts import render
# from Doctor.views import docpanel
from Doctor.forms import docregisterformA,docregisterformB
from Blood.views import home
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
#from django.http import HttpResponse
# from Doctor.forms import docregisterform

# Create your views here.
# def docpanel(request):
#     return render(request,'Doctor/doctorpanel.html',{})

def doclogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        docuser=authenticate(username=username,password=password)
        if docuser:
            if docuser.is_active:
                login(request,docuser)
                return HttpResponseRedirect(reverse('Doctor:docpanel'))
            else:
                return HttpResponse("Account not active")
        else:
            print("A login failed")
            return(HttpResponse("Invalid login details!"))
    else:
        return render(request,'Doctor/doctorlogin.html',{})

@login_required
def doclogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
 
def docregister(request):
    registered=False
    if request.method=='POST':
        formA=docregisterformA(data=request.POST)
        formB=docregisterformB(data=request.POST)
        if formA.is_valid() and formB.is_valid():
            docA=formA.save(commit=False)
            #print(formB.cleaned_data['username'])
            docA.set_password(docA.password)
            docA.save()
            docB=formB.save(commit=False)
            var=formA.cleaned_data['username']
            print(docA)
            docB.DocUser=docA
            docB.save()
            registered=True
            return HttpResponseRedirect(reverse('Doctor:doclogin'))
        else:
            print(docregisterformA.errors,docregisterformB.errors)
    else:
        formA=docregisterformA()
        formB=docregisterformB()
    return render(request,'Doctor/registration.html',{'formA':formA,'formB':formB,'registered':registered})

@login_required
def docpanel(request):
    return render(request,'Doctor/doctorpanel.html')

@login_required
def docpanelrequest(request):
    return render(request,'Doctor/doctorpanelrequest.html')

@login_required
def docpaneldonor(request):
    return render(request,'Doctor/doctorpaneldonor.html')

@login_required
def docpanelpatient(request):
    return render(request,'Doctor/doctorpanelpatient.html')

@login_required
def docpanelplist(request):
    return render(request,'Doctor/doctorpanelpatientlist.html')

@login_required
def docpanelrlist(request):
    return render(request,'Doctor/doctorpanelrequestlist.html')

