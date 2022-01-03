import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from application.functions import create_context
from .forms import OfferForm

TYPE_FREIGHT = ['furniture', 'animals', 'food', 'cars', 'medication', 'electronics', 'machinery']
FUEL_TYPE = ['benzine', 'diesel']
TRUCK_TYPE = ['truck', 'van', 'trailer', 'refrigerated truck']

# Create your views here.
# @login_required(login_url='login')
# def home(request):
#     gis = GIS()
#     map = gis.map("Palm Springs, CA")
#     return render(request, 'application/home.html', {'map': map})
from .models import Offer, Truck


@login_required(login_url='login')
def home(request):
    context = create_context(request)
    return render(request, 'application/home.html', context)


@login_required(login_url='login')
def account(request):
    context = create_context(request)
    return render(request, 'application/account.html', context)


@login_required(login_url='login')
def offer_view(request):
    offer = Offer()
    trucks = Truck.objects.all().filter(ownerId=request.user)
    sender = request.user.username.__str__()
    freight_type = TYPE_FREIGHT
    date = datetime.date.today()
    price_per_km = 0

    if request.method == "POST":
        offer.senderID = request.user
        offer.truckID = Truck.objects.all().get(id=request.POST.get("truckID"))
        offer.freight_type = request.POST.get("f_t")
        offer.date = request.POST.get('date')
        offer.price_per_km = request.POST.get('price_per_km')
        offer.save()

    context = {'trucks': trucks, 'sender': sender, 'f_t': freight_type, 'date': date,
               'price_per_km': price_per_km}
    return render(request, "application/create_offer.html", context)


@login_required(login_url='login')
def trucks(request):
    curr_trucks = Truck.objects.all().filter(ownerId=request.user)
    new_truck = Truck()

    if request.method == "POST":
        new_truck.ownerId = request.user
        new_truck.brand = request.POST.get('brand')
        new_truck.registration_plate = request.POST.get('reg_plt')
        new_truck.fuel = request.POST.get('fuel')
        new_truck.type = request.POST.get('type')
        new_truck.max_load = request.POST.get('max_load')
        new_truck.save()

    context = {'trucks': curr_trucks, 'fuel_t': FUEL_TYPE, 'truck_t': TRUCK_TYPE}
    return render(request, "application/trucks.html", context=context)


@login_required(login_url='login')
def create_request(request):
    context = create_context(request)
    return render(request, 'application/create_request.html', context)
