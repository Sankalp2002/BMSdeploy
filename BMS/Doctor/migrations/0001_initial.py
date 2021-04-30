# Generated by Django 3.2 on 2021-04-30 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=32)),
                ('age', models.PositiveIntegerField(default=18, help_text='Enter your age')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', help_text='Sex', max_length=1)),
                ('address', models.CharField(help_text='Enter your address', max_length=128)),
                ('phone', models.CharField(help_text='Enter your mobile number of 10 digits', max_length=10)),
                ('isApproved', models.CharField(choices=[('Y', 'Yes'), ('P', 'Pending')], default='P', max_length=1)),
                ('degree', models.CharField(help_text='Enter your Degree', max_length=32)),
                ('DocUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hospitalId', models.ForeignKey(help_text='Enter ID of your hospital', on_delete=django.db.models.deletion.CASCADE, to='Doctor.hospital')),
            ],
            options={
                'permissions': (('doctor_permission', "Can do the doctor's work"),),
            },
        ),
    ]
