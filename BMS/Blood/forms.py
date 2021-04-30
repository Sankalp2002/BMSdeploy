from django import forms
#from django.db import models
from Blood.models import BloodRequest,BRtype

class NewRequestForm(forms.ModelForm):
    class Meta:
        model=BloodRequest
        fields= ('patientId','quantity')

class NewRequestFormB(forms.ModelForm):
    class Meta:
        model=BRtype
        fields= ('bloodType',)

