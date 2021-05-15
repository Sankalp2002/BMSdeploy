# Donor
from django.db import models
from Doctor import models as dmodels
from Blood import models as bmodels
import datetime

# Create your models here.

class Donor(models.Model):
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
    donorId = models.CharField(primary_key=True,max_length=128,help_text="Donor ID is for unique identification.")
    doctorId = models.CharField(max_length=128,blank=True)
    name = models.CharField(max_length=32,help_text="Enter your name",blank=False)
    age = models.PositiveIntegerField(default=18, help_text="Enter your age",blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M',blank=False)
    address = models.CharField(max_length=128, help_text="Enter your address",blank=False)
    phone = models.CharField(max_length=10,help_text="Enter your mobile number of 10 digits",blank=False)
    email = models.EmailField(max_length=32,blank=False)
    bloodType = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES,blank=False)

    def __str__(self):
        return self.donorId
        


class Donation(models.Model):
    APPROVAL_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('P', 'Pending'),
    )
    donationId = models.AutoField(primary_key=True)
    donorId =  models.ForeignKey(Donor, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    # bloodType = models.CharField(max_length=3)
    isApproved = models.CharField(
        max_length=1, choices=APPROVAL_CHOICES, default='P')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.donationId
        # return str(self.donationId)+str(self.bloodType)

    class Meta:
        ordering=['-date']
