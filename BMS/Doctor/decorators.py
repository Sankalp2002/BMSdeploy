from django.core.exceptions import PermissionDenied
from Donor.models import Donor,Donation
from Patient.models import Patient
from Doctor.models import Doctor
from Blood.models import BloodRequest,BloodInventory
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse

def is_patients_doctor(function):
    def wrap(request, *args, **kwargs):
        entry = Patient.objects.get(pk=kwargs['pid'])
        if entry.doctorId == request.user.username:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_donors_doctor(function):
    def wrap(request, *args, **kwargs):
        entry = Donor.objects.get(pk=kwargs['did'])
        if entry.doctorId == request.user.username:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_doctor_approved(function):
    def wrap(request, *args, **kwargs):
        if request.user.groups.filter(name='DoctorGroup').exists():
            return function(request, *args, **kwargs)
        else:
            return HttpResponse("You are not approved by the ADMIN!")
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap