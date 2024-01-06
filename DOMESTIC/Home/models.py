from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactMe(models.Model):
    cno=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    text=models.CharField(max_length=100)
    
    def __str__(self):
        return self.uname

