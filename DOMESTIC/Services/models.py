from django.db import models
from datetime import date
# Create your models here.
class Cleaning(models.Model):
    sno = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=30)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    offer = models.CharField(default="", max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Services/images/cleaning')
    def __str__(self):
        return self.ServiceName
    
class Electics(models.Model):
    sno = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=30)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    offer = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Services/images/electrics')
    def __str__(self):
        return self.ServiceName

class Plumbing(models.Model):
    sno = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=30)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    offer = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Services/images/plumbing')
    def __str__(self):
        return self.ServiceName
    
class Carpenter(models.Model):
    sno = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=30)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    offer = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Services/images/carpenter')
    def __str__(self):
        return self.ServiceName



class Review(models.Model):
    sno=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=30)
    comment=models.TextField()
    rating=models.IntegerField(default=1)
    dt=models.DateField(default=date.today())

    def __str__(self):
        return self.uname