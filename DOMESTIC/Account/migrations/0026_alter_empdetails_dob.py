# Generated by Django 4.2 on 2023-04-11 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0025_delete_login_bookings_employee_empdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetails',
            name='dob',
            field=models.DateField(verbose_name=datetime.datetime),
        ),
    ]