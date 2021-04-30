from django import forms
#from django.db import models
from Blood.models import BloodRequest

class NewRequestForm(forms.ModelForm):
    class Meta:
        model=BloodRequest
        fields= ('patientId','bloodType','quantity')

