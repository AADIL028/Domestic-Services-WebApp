# Generated by Django 4.0.5 on 2023-03-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phone', models.DecimalField(decimal_places=10, max_digits=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]