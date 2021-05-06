from django.shortcuts import render
from Doctor.models import Doctor,Hospital
from Donor.models import Donor,Donation
from Patient.models import Patient
from Blood.models import BloodRequest,BloodInventory
from django.urls import reverse
from Doctor.forms import NewHospitalForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import ValidationError,validate_email
import re
from django.contrib.auth.models import Group

# Create your views here.
def valid_phone(data):
    reg="^(\d{10})$"
    if len(data)==10 and re.search(reg, data):
        print("valid")
    else:
        raise ValidationError(('Mobile Number must have 10 digits'))

def home(request):
    return render(request,'Blood/home.html')

@login_required
def adminlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Doctor:doclogin'))

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
    l=BloodInventory.objects.filter(bloodType=btype)
    if l.count()==0:
        message='Not enough stock of requested Blood Group!'
        requests=BloodRequest.objects.all().order_by('-requestId')
        return render(request,'Blood/adminpanelrequests.html',{'requests':requests,'m':message})

    obj2=BloodInventory.objects.get(bloodType=btype)
    q=obj.quantity
    message=""
    if obj2.unit<q:
        message='Not enough stock of requested Blood Group!'
        requests=BloodRequest.objects.all().order_by('-requestId')
        return render(request,'Blood/adminpanelrequests.html',{'requests':requests,'m':message})
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
    obj4=Donor.objects.get(donorId=obj.donorId)
    btype=obj4.bloodType
    q=obj.quantity
    if len(BloodInventory.objects.filter(bloodType=btype))==0:
        obj3=BloodInventory(bloodType=btype,unit=0)
        obj3.save()
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
    obj2=Doctor.objects.get(DocUser_id=did)
    i=obj2.DocUser.username
    dset=Donor.objects.filter(doctorId=i)
    for obj in dset:
        obj.doctorId="NULL"
        obj.save()
    pset=Patient.objects.filter(doctorId=i)
    for obj in pset:
        obj.doctorId="NULL"
        obj.save()
    User.objects.get(username=i).delete()
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
    g=Group.objects.get(name='DoctorGroup') 
    u=User.objects.get(username=obj.DocUser.username)
    u.groups.add(g)
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

@login_required
@user_passes_test(lambda u:u.is_superuser)
def newhospital(request):
    form=NewHospitalForm()
    if request.method=="POST":
        form= NewHospitalForm(request.POST)
        if form.is_valid():
            hos=form.save(commit=False)
            hos.save()
            return HttpResponseRedirect(reverse('Blood:adminpanel'))
        else:
            print('Error')
    return render(request,'Blood/addhospital.html',{'form':form})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def edithospital(request,id):
    doc=Hospital.objects.get(hospitalId=id)
    return render(request,'Blood/hospitaledit.html',{'doc':doc})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def listhospital(request):
    hos=Hospital.objects.all()
    return render(request,'Blood/hospitallist.html',{'hos':hos})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def delhospital(request,id):
    Hospital.objects.get(hospitalId=id).delete()
    return HttpResponseRedirect(reverse('Blood:listhospital'))

@login_required
@user_passes_test(lambda u:u.is_superuser)
def edithossave(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        doc=Hospital.objects.get(hospitalId=id)
        doc.name=name
        doc.address=address
        doc.save()
        return HttpResponseRedirect(reverse('Blood:listhospital'))
    else:
        doc=Hospital.objects.get(hospitalId=id)
        return render(request,'Blood/hospitaledit.html',{'doc':doc})

def errorview(request,e):
    e="Page not found!"
    return render(request,'Blood/error.html',{'e':e})

def error_404(request, exception):
   context = {}
   return render(request,'Blood/404.html', context)
