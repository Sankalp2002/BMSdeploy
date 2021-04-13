# Doctor
from django.db import models
from phone_field import PhoneField
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class Hospital(models.Model):
    hospitalId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)

    def str(self):
        return self.name


class Doctor(models.Model):
    DocUser = models.OneToOneField(User, on_delete=models.CASCADE)
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=32, help_text="Enter your name",blank=False)
    age = models.PositiveIntegerField(default=18, help_text="Enter your age")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    address = models.CharField(max_length=128, help_text="Enter your address")
    phone = PhoneField( help_text="Enter your phone number")
    # email = models.EmailField(
    #     max_length=32, help_text="Enter your email address")
    degree = models.CharField(max_length=32, help_text="Enter your Degree")
    hospitalId = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, help_text="Enter ID of your hospital")
    # username = models.CharField(
    #     max_length=32, help_text="Enter your username", primary_key=True)
    # password = models.CharField(max_length=1024, help_text="Atleast one each of digit,alphabet,special character required")
    #USERNAME_FIELD='username'
    def str(self):
        return self.DocUser.username
