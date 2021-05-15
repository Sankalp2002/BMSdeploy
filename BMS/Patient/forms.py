from django import forms
#from django.db import models
from Patient.models import Patient
from django.core.exceptions import ValidationError
import re

class NewPatientForm(forms.ModelForm):
        
    def clean_phone(self):
        data=self.cleaned_data['phone']
        reg="^(\d{10})$"
        if len(data)==10 and re.search(reg, data):
            print("valid")
        else:
            raise ValidationError(('Mobile Number must have 10 digits'))
        return data

    def clean_patientId(self):
        data=self.cleaned_data['patientId']
        reg="^[a-zA-Z0-9_-]*$"
        if re.search(reg, data):
            print("valid")
        else:
            raise ValidationError(('ID can only contain alphanumeric chars., underscore and hyphen!'))
        return data

    class Meta:
        model=Patient
        fields= ('patientId','name','address','phone','email','age','sex','bloodType')