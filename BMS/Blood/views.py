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
    donations=Donation.objects.all()
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
    requests=BloodRequest.objects.filter(isApproved='P')
    return render(request,'Blood/adminpanelrequests.html',{'requests':requests})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def appreqview(request,rid):
    obj=BloodRequest.objects.get(requestId=rid)
    btype=obj.bloodType
    q=obj.quantity
    obj2=BloodInventory.objects.get(bloodType=btype)
    if obj2.unit<q:
        return render(request,'Blood/adminpanelrequests.html')
    else:
        obj2.unit-=q
        obj2.save()
        obj.isApproved='Y'
        obj.save()
        return render(request,'Blood/adminpanelrequests.html')

@login_required
@user_passes_test(lambda u:u.is_superuser)
def rejreqview(request,rid):
    obj=BloodRequest.objects.get(requestId=rid)
    obj.isApproved='N'
    obj.save()
    return render(request,'Blood/adminpanelrequests.html')