# Generated by Django 4.0.5 on 2023-03-31 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_signup_delete_sigup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=20)),
                ('ServiceName', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(upload_to='Cart/images/')),
            ],
        ),
    ]