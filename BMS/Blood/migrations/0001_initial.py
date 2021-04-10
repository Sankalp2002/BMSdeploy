# Generated by Django 3.1.7 on 2021-04-10 13:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodInventory',
            fields=[
                ('bloodType', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('unit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('requestId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('bloodType', models.CharField(max_length=3)),
                ('isApproved', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('P', 'Pending')], default='P', max_length=1)),
                ('quantity', models.PositiveIntegerField()),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.doctor')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.patient')),
            ],
            options={
                'get_latest_by': '-self.date',
            },
        ),
    ]
