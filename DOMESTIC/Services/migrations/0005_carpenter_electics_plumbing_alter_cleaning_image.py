# Generated by Django 4.0.5 on 2023-03-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_cleaning_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpenter',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('ServiceName', models.CharField(max_length=30)),
                ('description1', models.CharField(max_length=200)),
                ('description2', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('offer', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='Services/images/carpenter')),
            ],
        ),
        migrations.CreateModel(
            name='Electics',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('ServiceName', models.CharField(max_length=30)),
                ('description1', models.CharField(max_length=200)),
                ('description2', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('offer', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='Services/images/electrics')),
            ],
        ),
        migrations.CreateModel(
            name='Plumbing',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('ServiceName', models.CharField(max_length=30)),
                ('description1', models.CharField(max_length=200)),
                ('description2', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('offer', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='Services/images/plumbing')),
            ],
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='image',
            field=models.ImageField(upload_to='Services/images/cleaning'),
        ),
    ]
