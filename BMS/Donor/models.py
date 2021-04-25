# Donor
from django.db import models
from Doctor import models as dmodels
from Blood import models as bmodels
from phone_field import PhoneField
import datetime
# Create your models here.


class Donor(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    donorId = models.AutoField(primary_key=True)
    doctorId = models.CharField(max_length=128)
    name = models.CharField(max_length=32,unique=True)
    address = models.CharField(max_length=128)
    phone = PhoneField(unique=True)
    email = models.EmailField(max_length=32)
    age = models.PositiveIntegerField(default=18)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    bloodType = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Donation(models.Model):
    APPROVAL_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('P', 'Pending'),
    )
    donationId = models.AutoField(primary_key=True)
    #donorId = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donorName =  models.ForeignKey(Donor, to_field='name', on_delete=models.CASCADE, default="Anonymous")
    date = models.DateField(default=datetime.date.today)
    bloodType = models.CharField(max_length=3)
    isApproved = models.CharField(
        max_length=1, choices=APPROVAL_CHOICES, default='P')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.donorName)
