from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Driver(models.Model):
    drivername=models.CharField(max_length=20)
    age=models.IntegerField()
    contact_no=models.IntegerField()
    bus_no=models.IntegerField()

    # def __str__(self):
    #     return drivername
class User(models.Model):
    ADMIN = "ADMIN"
    DRIVER = "DRIVER"
    CUSTOMER = "CUSTOMER"

    DESIGNATION_CHOICES = ((ADMIN, "ADMIN"), (DRIVER, "DRIVER"),(CUSTOMER, "CUSTOMER"))

    user_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20,choices=DESIGNATION_CHOICES,default=" ")


class Customer(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    phone=models.PositiveBigIntegerField()
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()


class Account(AbstractUser):
    is_admin= models.BooleanField('Is admin')
    is_customer = models.BooleanField('Is customer')
    is_employee = models.BooleanField('Is employee')


class Employee(models.Model):
    ename=models.CharField(max_length=20)
    eage=models.IntegerField()
