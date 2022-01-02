from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _


# Create your models here.
# class FuelType(models.TextChoices):
#     BENZINE = 'benzine'
#     DIESEL = 'diesel'


# class TruckType(models.TextChoices):
#     TRUCK = 'truck'  # tir
#     VAN = 'van'  # duba
#     REFRIGERATED_TRUCK = 'refrigerated truck'  # camion frigorific
#     TRAILER = 'trailer'  # platforma


# class FreightType(models.TextChoices):
#     FURNITURE = 'furniture'
#     ANIMALS = 'animals'
#     FOOD = 'food'
#     CARS = 'cars'
#     MEDICATION = 'medication'
#     ELECTRONICS = 'electronics'
#     MACHINERY = 'machinery'

# class FreightType(models.TextChoices):
#     FURNITURE = 'F', _('furniture')
#     ANIMALS = 'A', _('animals')
#     FOOD = 'FO', _('food')
#     CARS = 'C', _('cars')
#     MEDICATION = 'M', _('medication')
#     ELECTRONICS = 'E', _('electronics')
#     MACHINERY = 'MA', _('machinery')


class Truck(models.Model):
    class FuelType(models.TextChoices):
        BENZINE = 'B', _('benzine')
        DIESEL = 'D', _('diesel')

    class TruckType(models.TextChoices):
        TRUCK = 'T', _('truck')  # tir
        VAN = 'V', _('van')  # duba
        REFRIGERATED_TRUCK = 'R', _('refrigerated truck')  # camion frigorific
        TRAILER = 'TR', _('trailer')  # platforma

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, choices=TruckType.choices)
    brand = models.CharField(max_length=20)
    registration_plate = models.CharField(max_length=15, unique=True)
    fuel = models.CharField(max_length=10, choices=FuelType.choices)
    max_load = models.IntegerField()
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(User, on_delete=models.CASCADE)
    source = {
        'latitude': models.FloatField(),
        'longitude': models.FloatField()
    }
    destination = {
        'latitude': models.FloatField(),
        'longitude': models.FloatField()
    }
    registration_date = models.DateField(auto_now_add=True)
    arrival_date = models.DateField()
    max_price = models.FloatField()
    freight_type = models.CharField(max_length=15)
    weight = models.IntegerField()


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    truckID = models.ForeignKey(Truck, on_delete=models.CASCADE)
    freight_type = models.CharField(max_length=15)
    date = models.DateField()
    price_per_km = models.FloatField()


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    transporterID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transporter')
    senderID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    truckID = models.ForeignKey(Truck, on_delete=models.CASCADE)
    source = {
        'latitude': models.FloatField(),
        'longitude': models.FloatField()
    }
    destination = {
        'latitude': models.FloatField(),
        'longitude': models.FloatField()
    }
    date = models.DateField(auto_now_add=True)
    freight_type = models.TextField(max_length=15)
    final_price = models.FloatField()
    km = models.FloatField()
