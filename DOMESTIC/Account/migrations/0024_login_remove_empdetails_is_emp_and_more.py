# Generated by Django 4.2 on 2023-04-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0023_alter_empdetails_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='empdetails',
            name='is_emp',
        ),
        migrations.RemoveField(
            model_name='empdetails',
            name='username',
        ),
        migrations.AlterField(
            model_name='empdetails',
            name='fname',
            field=models.CharField(max_length=20),
        ),
    ]