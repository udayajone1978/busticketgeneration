from django.db import models


class bus(models.Model):
    bus_name=models.CharField(max_length=20)
    bus_num=models.IntegerField()
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
    phone=models.PositiveBigIntegerField()
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

from django.contrib.auth.models import Group
class Mymodel(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)

class busdriver(models.Model):
    fk=models.ForeignKey(bus,on_delete=models.CASCADE)

@property
def name(self):
    return self.fk.bus_name

@property
def num(self):
    return self.fk.bus_num