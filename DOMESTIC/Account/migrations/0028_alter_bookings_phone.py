# Generated by Django 4.0.5 on 2023-04-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0027_alter_empdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
    ]