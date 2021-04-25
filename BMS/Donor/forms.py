from django import forms
#from django.db import models
from Donor.models import Donor

class NewDonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields= ('doctorId','name','address','phone','email','age','sex','bloodType')