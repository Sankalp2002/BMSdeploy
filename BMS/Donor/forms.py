from django import forms
#from django.db import models
from Donor.models import Donor,Donation
from django.core.exceptions import ValidationError
import re

class NewDonorForm(forms.ModelForm):
    def clean_phone(self):
        data=self.cleaned_data['phone']
        reg="^(\d{10})$"
        if len(data)==10 and re.search(reg, data):
            print("valid")
        else:
            raise ValidationError(('Mobile Number must have 10 digits'))
        return data

    class Meta:
        model=Donor
        fields= ('name','address','phone','email','age','sex','bloodType')

class NewDonationForm(forms.ModelForm):
    class Meta:
        model=Donation
        fields= ('donorName','date','quantity')