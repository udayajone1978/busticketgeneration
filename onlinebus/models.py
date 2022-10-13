from django.db import models

class bus_num(models.Model):
    bus_no = models.IntegerField()
class bus(models.Model):
    bus_name=models.CharField(max_length=20)
    bus_no=models.IntegerField()
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=30)
    seats=models.IntegerField()
    balanseat=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField()
    time =models.TimeField()

class consumer(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    phone=models.PositiveBigIntegerField(unique=True)
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

class driver(models.Model):
    drivername=models.CharField(max_length=20)
    age=models.IntegerField()
    contact_no=models.IntegerField()
    bus_no=models.ForeignKey(bus_num,on_delete=models.CASCADE)

from django.contrib.auth.models import Group
class Mymodel(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)


