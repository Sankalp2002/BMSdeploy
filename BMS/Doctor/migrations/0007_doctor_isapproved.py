# Generated by Django 3.2 on 2021-04-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0006_alter_doctor_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='isApproved',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('P', 'Pending')], default='P', max_length=1),
        ),
    ]