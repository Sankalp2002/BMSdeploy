from django.shortcuts import render
from django.db import models
from Doctor.forms import docregisterformA,docregisterformB
from Donor.forms import NewDonorForm,NewDonationForm
from Blood.forms import NewRequestForm
from Patient.forms import NewPatientForm
from Blood.views import home,adminpanel,errorview
from Donor.models import Donor,Donation
from Patient.models import Patient
from Doctor.models import Doctor
from Blood.models import BloodRequest,BloodInventory
from . import forms
from Doctor.decorators import is_doctor_approved,is_donors_doctor,is_patients_doctor
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.validators import ValidationError,validate_email
import re
#from django.http import HttpResponse
# from Doctor.forms import docregisterform

# Create your views here.

def valid_phone(data):
    reg="^(\d{10})$"
    if len(data)==10 and re.search(reg, data):
        print("valid")
    else:
        raise ValidationError(('Mobile Number must have 10 digits'))

# def valid_age(data):
#     if data>70:
#         raise ValidationError(('You are gonna die soon'))
#     if data<18:
#         raise ValidationError(('Too young to donate blood'))
#     return data

# def valid_Id(data):
#     reg="^[a-zA-Z0-9_-]*$"
#     if re.search(reg, data):
#         print("valid")
#     else:
#         raise ValidationError(('ID can only contain alphanumeric chars., underscore and hyphen!'))
#     return data

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
            e="Invalid Login Details!"
            return render(request,'Blood/error.html',{'e':e})
    else:
        return render(request,'Doctor/doctorlogin.html')

@login_required
def doclogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Doctor:doclogin'))
 
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
            m="Registration Successful"
            return render(request,'Doctor/doctorlogin.html',{'m':m})
        else:
            print(docregisterformA.errors,docregisterformB.errors)
    else:
        formA=docregisterformA()
        formB=docregisterformB()
    return render(request,'Doctor/registration.html',{'formA':formA,'formB':formB,'registered':registered})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def docpanel(request):
    return render(request,'Doctor/doctorpanel.html')

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def docpanelrequest(request):
    form=NewRequestForm()
    if request.method=="POST":
        form= NewRequestForm(request.POST)
        if form.is_valid():
            req=form.save(commit=False)
            obj=Patient.objects.get(patientId=req.patientId)
            if obj.doctorId==request.user.username:
                req.save()
                return docpanel(request)
            else:
                raise(ValidationError("You are not the doctor of chosen patient."))
        else:
            print('Error')
    return render(request,'Doctor/doctorpanelrequest.html',{'form':form})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def docpanelnewdon(request):
    form=NewDonationForm()
    if request.method=="POST":
        form= NewDonationForm(request.POST)
        if form.is_valid():
            donat=form.save(commit=False)
            obj=Donor.objects.get(donorId=donat.donorId)
            donat.bloodType=obj.bloodType
            donat.save()
            return docpanel(request)
        else:
            print('Error')
    return render(request,'Doctor/doctorpanelnewdon.html',{'form':form})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
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
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
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
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def docpanelplist(request):
    patients=Patient.objects.filter(doctorId=request.user.username)
    return render(request,'Doctor/doctorpanelpatientlist.html',{'patients':patients})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def docpanelrlist(request):
    plist=Patient.objects.filter(doctorId=request.user.username).values_list('patientId',flat=True)
    # pset=set(plist)
    requests=BloodRequest.objects.filter(patientId__in=plist).order_by('-requestId')
    return render(request,'Doctor/doctorpanelrequestlist.html',{'requests':requests})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def docpaneldlist(request):
    donors=Donor.objects.filter(doctorId=request.user.username)
    return render(request,'Doctor/doctorpaneldonorlist.html',{'donors':donors})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
@is_patients_doctor
def delpatview(request,pid):
    Patient.objects.get(patientId=pid).delete()
    return HttpResponseRedirect(reverse('Doctor:docpanelplist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
@is_donors_doctor
def deldonview(request,did):
    Donor.objects.get(donorId=did).delete()
    return HttpResponseRedirect(reverse('Doctor:docpaneldlist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def cancelreq(request,rid):
    BloodRequest.objects.get(requestId=rid).delete()
    return HttpResponseRedirect(reverse('Doctor:docpanelrlist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
@is_donors_doctor
def editdonview(request,did):
    don=Donor.objects.get(donorId=did)
    return render(request,'Doctor/editdonor.html',{'don':don})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
@is_donors_doctor
def editdonsave(request,did):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        phone=request.POST.get('phone')
        valid_phone(phone)
        address=request.POST.get('address')
        e=request.POST.get('email')
        validate_email(e)
        don=Donor.objects.get(donorId=did)
        don.name=name
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
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
@is_patients_doctor
def editpatview(request,pid):
    pat=Patient.objects.get(patientId=pid)
    return render(request,'Doctor/editpatient.html',{'pat':pat})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
@is_patients_doctor
def editpatsave(request,pid):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        phone=request.POST.get('phone')
        valid_phone(phone)
        address=request.POST.get('address')
        e=request.POST.get('email')
        validate_email(e)
        pat=Patient.objects.get(patientId=pid)
        pat.name=name
        pat.age=age
        pat.sex=sex
        pat.phone=phone
        pat.address=address
        pat.email=e
        pat.save()
        return HttpResponseRedirect(reverse('Doctor:docpanelplist'))
    else:
        pat=Patient.objects.get(patientId=pid)
        return render(request,'Doctor/editpatient.html',{'pat':pat})

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def editpatcancel(request):
    return HttpResponseRedirect(reverse('Doctor:docpanelplist'))

@login_required
@user_passes_test(lambda u:not u.is_superuser )
@is_doctor_approved
def editdoncancel(request):
    return HttpResponseRedirect(reverse('Doctor:docpaneldlist'))