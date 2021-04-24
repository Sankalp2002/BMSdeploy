from django import forms
#from django.db import models
from Donor.models import Donor
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class NewDonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields= ('doctorId','name','address','phone','email','age','sex','bloodType')