# Doctor
from django.db import models
from phone_field import PhoneField
# Create your models here.


class Hospital(models.Model):
    hospitalId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)

    def str(self):
        return self.hospitalId


class Doctor(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=32, help_text="Enter your name")
    age = models.PositiveIntegerField(default=18, help_text="Enter your age")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    address = models.CharField(max_length=128, help_text="Enter your address")
    phone = PhoneField(
        blank=True, help_text="Enter your phone number", unique=True)
    email = models.EmailField(
        max_length=32, help_text="Enter your email address")
    degree = models.CharField(max_length=32, help_text="Enter your Degree")
    hospitalId = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, help_text="Enter ID of your hospital")
    doctorId = models.CharField(
        max_length=32, help_text="Enter your username", primary_key=True)
    password = models.CharField(
        max_length=32, help_text="Atleast one each of digit,alphabet,special character required")

    def str(self):
        return self.doctorId
