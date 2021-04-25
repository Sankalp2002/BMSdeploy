from django import forms
#from django.db import models
from Donor.models import Donor,Donation

class NewDonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields= ('name','address','phone','email','age','sex','bloodType')

class NewDonationForm(forms.ModelForm):
    class Meta:
        model=Donation
        fields= ('donorName','date','quantity')