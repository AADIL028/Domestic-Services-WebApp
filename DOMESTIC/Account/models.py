from django.db import models
import datetime
from django.contrib.auth.models import User
import datetime



class Signup(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    fname= models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=50,default="Ahmedabad")
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username

    

class Empdetails(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,default="EMP_")
    fname= models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=30)
    address= models.CharField(max_length=50)
    work=models.CharField(max_length=30)
    password = models.CharField(max_length=25)
    dob=models.DateField(datetime.datetime)
    def __str__(self):
        return self.username
    
class Bookings(models.Model):
    BookingId = models.AutoField(primary_key=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Employee = models.CharField(max_length=100)
    category = models.CharField(max_length=500)
    sno = models.CharField(max_length=50)
    price = models.IntegerField()
    booking_date = models.DateField(default=datetime.datetime.today)
    service_date = models.DateField()
    slote = models.CharField(max_length=20)
    name = models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    phone = models.BigIntegerField(default=0)
    complete_status = models.BooleanField(default=False)
    cancel_booking = models.BooleanField(default=False)
    otp = models.IntegerField(default=0000)

    def __str__(self):
        return str(self.BookingId)
