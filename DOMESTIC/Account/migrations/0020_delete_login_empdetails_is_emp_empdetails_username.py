# Generated by Django 4.2 on 2023-04-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0019_bookings_cancel_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='empdetails',
            name='is_emp',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='empdetails',
            name='username',
            field=models.CharField(default=1, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
