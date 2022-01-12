from datetime import datetime

from django.db import models
from django.contrib.auth.models import Group, User
from django.utils import timezone


class Truck(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    registration_plate = models.CharField(max_length=15, unique=True)
    fuel = models.CharField(max_length=10)
    max_load = models.IntegerField()
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.TextField(max_length=25)
    destination = models.TextField(max_length=25)
    departure_date = models.DateField(default=timezone.now())
    arrival_date = models.DateField(default=timezone.now())
    max_price = models.FloatField(default=0)
    freight_type = models.CharField(max_length=15)
    weight = models.IntegerField()
    phone = models.CharField(max_length=11, default='0')
    email = models.CharField(max_length=50, default='a')
    other_details = models.CharField(max_length=200, default='a')


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    truckID = models.ForeignKey(Truck, on_delete=models.CASCADE)
    freight_type = models.CharField(max_length=15)
    price_per_km = models.FloatField(default=0)
    price_per_km_emptyTruck = models.FloatField(default=0)
    departure_date = models.DateField(default=timezone.now())
    source = models.CharField(max_length=30, default='a')
    arrival_date = models.DateField(default=timezone.now())
    destination = models.CharField(max_length=30, default='a')
    phone = models.CharField(max_length=11, default='0')
    email = models.CharField(max_length=50, default='a')
    other_details = models.CharField(max_length=200, default='a')


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    transporterID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transporter')
    senderID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    truckID = models.ForeignKey(Truck, on_delete=models.CASCADE)
    source = models.TextField(max_length=25)
    destination = models.TextField(max_length=25)
    date = models.DateField(auto_now_add=True)
    freight_type = models.TextField(max_length=15)
    final_price = models.FloatField()
    km = models.FloatField()
