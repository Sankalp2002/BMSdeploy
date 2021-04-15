from django import forms
#from django.db import models
from Doctor.models import Doctor
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class docregisterformA(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())
    class Meta:
        model=User
        fields=('username','email','password')

class docregisterformB(forms.ModelForm):
    class Meta():
        model=Doctor
        fields=('name','age','sex','address','phone','degree','hospitalId')


# class docloginform(forms.Form):
#     doctorId = forms.CharField(
#         max_length=32, help_text="Enter your username")
#     password = forms.CharField(
#         max_length=32, help_text="Atleast one each of digit,alphabet,special character required")





        # name=forms.CharField(required=True,max_length=20,min_length=5)
    # address=forms.CharField(required=True,max_length=100,min_length=5)
    # phone=forms.PhoneField(required=True)
    # age=forms.IntegerField(required=True)
    # sex=forms.ChoiceField(required=True)
    # email=forms.EmailField(required=True,max_length=30)
    # degree=forms.CharField(required=True,max_length=40,min_length=5)
    # hospital_id=forms.CharField(required=True,max_length=20)
    # password=forms.CharField(required=True)
    
    # def clean_name(self):
    #     data=self.cleaned_data['name']
    #     return data

    # def clean_address(self):
    #     data=self.cleaned_data['address']
    #     return data

    # def clean_phone(self):
    #     data=self.cleaned_data['phone']
    #     return data

    # def clean_age(self):
    #     data=self.cleaned_data['age']
    #     if data>80:
    #         raise ValidationError(_('You are gonna die soon'))
    #     if data<18:
    #         raise ValidationError(_('Too young to be a doctor'))
    #     return data

    # def clean_sex(self):
    #     data=self.cleaned_data['sex']
    #     return data

    # def clean_email(self):
    #     data=self.cleaned_data['email']
    #     return data

    #  def clean_degree(self):
    #     data=self.cleaned_data['degree']
    #     return data

    #  def clean_hospital_id(self):
    #     data=self.cleaned_data['hospital_id']
    #     return data

    #  def clean_password(self):
    #     data=self.cleaned_data['password']
    #     if len(data)>32:
    #         raise ValidationError(_('Password is too long'))
    #     if len(data)<8:
    #         raise ValidationError(_('Password is too short'))
    #     special_characters = "[~\!@#\$%\^&\*\(\)_\+\{\}\\":;'\[\]]"
    #     if not any(char.isdigit() for char in data):
    #         raise ValidationError(_('Password must contain at least 1 digit'))
    #     if not any(char.isalpha() for char in password):
    #         raise ValidationError(_('Password must contain at least 1 alphabet'))
    #     if not any(char in special_characters for char in password):
    #         raise ValidationError(_('Password must contain at least 1 special character'))
    #     return data

        
    # SEX_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Other'),
    # )
    # name = forms.CharField(max_length=32, help_text="Enter your name")
    # age = forms.PositiveIntegerField(default=18, help_text="Enter your age")
    # sex = forms.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    # address = forms.CharField(max_length=128, help_text="Enter your address")
    # phone = PhoneField( help_text="Enter your phone number", unique=True)
    # degree = forms.CharField(max_length=32, help_text="Enter your Degree")
    # hospitalId = forms.ForeignKey(
    #     Hospital, on_delete=models.CASCADE, help_text="Enter ID of your hospital")