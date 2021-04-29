# Patient
from django.db import models
from Doctor import models as dmodels
from django.core.exceptions import ValidationError
import re
# Create your models here.

class Patient(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    patientId = models.AutoField(primary_key=True)
    doctorId = models.CharField(max_length=128,blank=True)
    name = models.CharField(max_length=32, help_text="Enter your name",blank=False)
    age = models.PositiveIntegerField(default=18, help_text="Enter your age")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    address = models.CharField(max_length=128, help_text="Enter your address")
    phone = models.CharField(max_length=10,help_text="Enter your mobile number of 10 digits")
    email = models.EmailField(max_length=32)
    bloodType = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES)

    def __str__(self):
        return self.name
