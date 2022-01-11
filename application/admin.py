from django.contrib import admin
from application.models import Truck, Request, Offer, Contract

# Register your models here.

admin.site.register(Truck)
admin.site.register(Request)
admin.site.register(Offer)
admin.site.register(Contract)
