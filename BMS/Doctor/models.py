# Doctor
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
# Create your models here.

class Hospital(models.Model):
    hospitalId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    DocUser = models.OneToOneField(User, on_delete=models.CASCADE)
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    APPROVAL_CHOICES = (
        ('Y', 'Yes'),
        ('P', 'Pending'),
    )
    name = models.CharField(max_length=32, help_text="Enter your name",blank=False)
    age = models.PositiveIntegerField(default=18, help_text="Enter your age")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M',help_text="Sex")
    address = models.CharField(max_length=128, help_text="Enter your address")
    phone = models.CharField(max_length=10,help_text="Enter your mobile number of 10 digits")
    isApproved = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='P')
    degree = models.CharField(max_length=32, help_text="Enter your Degree")
    hospitalId = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, help_text="Enter ID of your hospital")
    class Meta:
        permissions=(
            ("is_doctor","Has been registered."),
            ("is_approved","Can do the doctor's work"),
        )
    def __str__(self):
        return self.DocUser.username
