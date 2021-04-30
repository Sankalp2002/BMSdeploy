# Blood
from django.db import models
from Patient import models as pmodels
from Doctor import models as dmodels
from Blood import models as bmodels
import datetime
# Create your models here.


class BloodInventory(models.Model):
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
    bloodType = models.CharField(max_length=3, primary_key=True,choices=BLOOD_GROUP_CHOICES)
    unit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.bloodType


class BRtype(models.Model):
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
    
    bloodType = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES,help_text="Enter the Blood Group required")

    def __str__(self):
        return self.bloodType

class BloodRequest(models.Model):
    APPROVAL_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('P', 'Pending'),
    )
    requestId = models.AutoField(primary_key=True)
    patientId = models.ForeignKey(pmodels.Patient, on_delete=models.CASCADE,help_text="Patient")
    # doctorId = models.CharField(max_length=128,blank=True)
    date = models.DateField(default=datetime.date.today)
    # bloodType = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES,help_text="Enter the Blood Group required")
    btype = models.OneToOneField(BRtype,on_delete=models.CASCADE,null=True)
    isApproved = models.CharField(
        max_length=1, choices=APPROVAL_CHOICES, default='P')
    quantity = models.PositiveIntegerField(help_text="Enter quantity of Blood required")

    def __str__(self):
        return str(self.requestId)

    class Meta:
        ordering=['-date']

