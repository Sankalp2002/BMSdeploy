# Patient
from django.db import models
from Doctor import models as dmodels
from phone_field import PhoneField
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
    doctorId = models.CharField(max_length=128)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    phone = PhoneField(unique=True)
    email = models.EmailField(max_length=32)
    age = models.PositiveIntegerField(default=18)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    bloodType = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES)

    def __str__(self):
        return self.name
