from django import forms
#from django.db import models
from Patient.models import Patient

class NewPatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields= ('doctorId','name','address','phone','email','age','sex','bloodType')