# Blood
from django.db import models
from Patient import models as pmodels
from Doctor import models as dmodels
import datetime
# Create your models here.


class BloodInventory(models.Model):
    bloodType = models.CharField(max_length=3, primary_key=True)
    unit = models.PositiveIntegerField(default=0)

    def str(self):
        return self.bloodType


class BloodRequest(models.Model):
    APPROVAL_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('P', 'Pending'),
    )
    requestId = models.AutoField(primary_key=True)
    patientId = models.ForeignKey(pmodels.Patient, on_delete=models.CASCADE)
    doctorId = models.ForeignKey(dmodels.Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    bloodType = models.CharField(max_length=3)
    isApproved = models.CharField(
        max_length=1, choices=APPROVAL_CHOICES, default='P')
    quantity = models.PositiveIntegerField()

    def str(self):
        return self.requestId

    class Meta:
        get_latest_by = "-self.date"
