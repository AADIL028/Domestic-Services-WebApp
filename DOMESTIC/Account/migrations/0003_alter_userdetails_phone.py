# Generated by Django 4.1.2 on 2023-03-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_userdetails_password_alter_userdetails_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
