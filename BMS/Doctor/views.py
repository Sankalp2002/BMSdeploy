from django.shortcuts import render
from django.db import models
# from Doctor.views import docpanel
from Doctor.forms import docregisterformA,docregisterformB
from Donor.forms import NewDonorForm,NewDonationForm
from Blood.forms import NewRequestForm
from Patient.forms import NewPatientForm
from Blood.views import home,adminpanel
from Donor.models import Donor,Donation
from Patient.models import Patient
from Doctor.models import Doctor
from Blood.models import BloodRequest,BloodInventory
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
#from django.http import HttpResponse
# from Doctor.forms import docregisterform

# Create your views here.

def doclogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        docuser=authenticate(username=username,password=password)
        if docuser:
            if docuser.is_active and docuser.is_superuser:
                login(request,docuser)
                return HttpResponseRedirect(reverse('Blood:adminpanel'))
            elif docuser.is_active:
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
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpanel(request):
    return render(request,'Doctor/doctorpanel.html')

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpanelrequest(request):
    form=NewRequestForm()
    if request.method=="POST":
        form= NewRequestForm(request.POST)
        if form.is_valid():
            req=form.save(commit=False)
            req.doctorId=request.user.username
            req.save()
            return docpanel(request)
        else:
            print('Error')
    return render(request,'Doctor/doctorpanelrequest.html',{'form':form})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpanelnewdon(request):
    form=NewDonationForm()
    if request.method=="POST":
        form= NewDonationForm(request.POST)
        if form.is_valid():
            donat=form.save(commit=False)
            obj=Donor.objects.get(name=donat.donorName)
            donat.bloodType=obj.bloodType
            donat.save()
            return docpanel(request)
        else:
            print('Error')
    return render(request,'Doctor/doctorpanelnewdon.html',{'form':form})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpaneldonor(request):
    form=NewDonorForm()
    if request.method=="POST":
        form= NewDonorForm(request.POST)
        if form.is_valid():
            don=form.save(commit=False)
            don.doctorId=request.user.username
            don.save()
            return docpanel(request)
        else:
            print('Error')
    return render(request,'Doctor/doctorpaneldonor.html',{'form':form})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpanelpatient(request):
    form=NewPatientForm()
    if request.method=="POST":
        form= NewPatientForm(request.POST)
        if form.is_valid():
            pat=form.save(commit=False)
            pat.doctorId=request.user.username
            pat.save()
            return docpanel(request)
        else:
            print('Error')
    return render(request,'Doctor/doctorpanelpatient.html',{'form':form})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpanelplist(request):
    patients=Patient.objects.filter(doctorId=request.user.username)
    return render(request,'Doctor/doctorpanelpatientlist.html',{'patients':patients})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpanelrlist(request):
    requests=BloodRequest.objects.filter(doctorId=request.user.username).order_by('-requestId')
    return render(request,'Doctor/doctorpanelrequestlist.html',{'requests':requests})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def docpaneldlist(request):
    donors=Donor.objects.filter(doctorId=request.user.username)
    return render(request,'Doctor/doctorpaneldonorlist.html',{'donors':donors})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def delpatview(request,pid):
    Patient.objects.get(patientId=pid).delete()
    return HttpResponseRedirect(reverse('Doctor:docpanelplist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def deldonview(request,pid):
    Donor.objects.get(donorId=pid).delete()
    return HttpResponseRedirect(reverse('Doctor:docpaneldlist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def cancelreq(request,rid):
    BloodRequest.objects.get(requestId=rid).delete()
    return HttpResponseRedirect(reverse('Doctor:docpanelrlist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def editdonview(request,did):
    don=Donor.objects.get(donorId=did)
    return render(request,'Doctor/editdonor.html',{'don':don})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def editdonsave(request,did):
    if request.method=='POST':
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        e=request.POST.get('email')
        don=Donor.objects.get(donorId=did)
        don.age=age
        don.sex=sex
        don.phone=phone
        don.address=address
        don.email=e
        don.save()
        return HttpResponseRedirect(reverse('Doctor:docpaneldlist'))
    else:
        don=Donor.objects.get(donorId=did)
        return render(request,'Doctor/editdonor.html',{'don':don})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def editpatview(request,did):
    pat=Patient.objects.get(patientId=did)
    return render(request,'Doctor/editpatient.html',{'pat':pat})

@login_required
@user_passes_test(lambda u:not u.is_superuser and Doctor.objects.get(id=u.id).isApproved=='Y')
def editpatsave(request,did):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        e=request.POST.get('email')
        pat=Patient.objects.get(patientId=did)
        pat.name=name
        pat.age=age
        pat.sex=sex
        pat.phone=phone
        pat.address=address
        pat.email=e
        pat.save()
        return HttpResponseRedirect(reverse('Doctor:docpanelplist'))
    else:
        pat=Patient.objects.get(patientId=did)
        return render(request,'Doctor/editpatient.html',{'pat':pat})
