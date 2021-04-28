from django.shortcuts import render
from Doctor.models import Doctor
from Donor.models import Donor,Donation
from Patient.models import Patient
from Blood.models import BloodRequest,BloodInventory
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import ValidationError,validate_email
import re

# Create your views here.
def valid_phone(data):
    reg="^(\d{10})$"
    if len(data)==10 and re.search(reg, data):
        print("valid")
    else:
        raise ValidationError(('Mobile Number must have 10 digits'))

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
    inventory=BloodInventory.objects.all()
    return render(request,'Blood/adminpanel.html',{'inventory':inventory})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpaneldoctor(request):
    doctors=Doctor.objects.all()
    return render(request,'Blood/adminpaneldoctor.html',{'doctors':doctors})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpaneldonations(request):
    donations=Donation.objects.all().order_by('-donationId')
    return render(request,'Blood/adminpaneldonations.html',{'donations':donations})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpaneldonors(request):
    donors=Donor.objects.all()
    return render(request,'Blood/adminpaneldonors.html',{'donors':donors})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpanelpatients(request):
    patients=Patient.objects.all()
    return render(request,'Blood/adminpanelpatients.html',{'patients':patients})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminpanelrequests(request):
    requests=BloodRequest.objects.all().order_by('-requestId')
    return render(request,'Blood/adminpanelrequests.html',{'requests':requests})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def appreqview(request,qid):
    obj=BloodRequest.objects.get(requestId=qid)
    btype=obj.bloodType
    obj2=BloodInventory.objects.get(bloodType=btype)
    q=obj.quantity
    if obj2.unit<q:
        return HttpResponseRedirect(reverse('Blood:adminpanelrequests'))
    else:
        q=obj.quantity
        obj2.unit-=q
        obj2.save()
        obj.isApproved='Y'
        obj.save()
        return HttpResponseRedirect(reverse('Blood:adminpanelrequests'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def rejreqview(request,rid):
    obj=BloodRequest.objects.get(requestId=rid)
    obj.isApproved='N'
    obj.save()
    return HttpResponseRedirect(reverse('Blood:adminpanelrequests'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def appdonview(request,did):
    obj=Donation.objects.get(donationId=did)
    btype=obj.bloodType
    q=obj.quantity
    obj2=BloodInventory.objects.get(bloodType=btype)
    obj2.unit+=q
    obj2.save()
    obj.isApproved='Y'
    obj.save()
    return HttpResponseRedirect(reverse('Blood:adminpaneldonations'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def rejdonview(request,did):
    obj=Donation.objects.get(donationId=did)
    obj.isApproved='N'
    obj.save()
    return HttpResponseRedirect(reverse('Blood:adminpaneldonations'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def deldocview(request,did):
    Doctor.objects.get(DocUser_id=did).delete()
    return HttpResponseRedirect(reverse('Blood:adminpaneldoctor'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def deldonview(request,did):
    Donor.objects.get(donorId=did).delete()
    return HttpResponseRedirect(reverse('Blood:adminpaneldonors'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def delpatview(request,pid):
    Patient.objects.get(patientId=pid).delete()
    return HttpResponseRedirect(reverse('Blood:adminpanelpatients'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def appdocview(request,did):
    obj=Doctor.objects.get(DocUser_id=did)
    obj.isApproved='Y'
    obj.save()
    return HttpResponseRedirect(reverse('Blood:adminpaneldoctor'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def editdocview(request,did):
    doc=Doctor.objects.get(DocUser_id=did)
    return render(request,'Blood/editdoctor.html',{'doc':doc})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def editdocsave(request,did):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        degree=request.POST.get('degree')
        phone=request.POST.get('phone')
        valid_phone(phone)
        address=request.POST.get('address')
        doc=Doctor.objects.get(DocUser_id=did)
        doc.name=name
        doc.age=age
        doc.sex=sex
        doc.degree=degree
        doc.phone=phone
        doc.address=address
        doc.save()
        return HttpResponseRedirect(reverse('Blood:adminpaneldoctor'))
    else:
        doc=Doctor.objects.get(DocUser_id=did)
        return render(request,'Blood/editdoctor.html',{'doc':doc})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def editdoccancel(request):
    return HttpResponseRedirect(reverse('Blood:adminpaneldoctor'))