import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse
from application.functions import create_context
from .decorators import allowed_users
from .forms import OfferForm
from datetime import date

TYPE_FREIGHT = ['furniture', 'animals', 'food', 'cars', 'medication', 'electronics', 'machinery']
FUEL_TYPE = ['benzine', 'diesel']
TRUCK_TYPE = ['truck', 'van', 'trailer', 'refrigerated truck']

# Create your views here.
# @login_required(login_url='login')
# def home(request):
#     gis = GIS()
#     map = gis.map("Palm Springs, CA")
#     return render(request, 'application/home.html', {'map': map})
from .models import Offer, Truck, Request


@login_required(login_url='login')
def home(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    context = {'user_groups': user_groups}
    return render(request, 'application/main_layout_application.html', context)


@login_required(login_url='login')
def account(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    context = {'user_groups': user_groups}
    return render(request, 'application/account.html', context)


@allowed_users(allowed_roles=['transportator'])
@login_required(login_url='login')
def offer_view(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
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

    context = {'user_groups': user_groups,
               'trucks': trucks,
               'sender': sender,
               'f_t': freight_type,
               'date': date,
               'price_per_km': price_per_km}
    return render(request, "application/create_offer.html", context)


@login_required(login_url='login')
def trucks(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]

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

    context = {'user_groups': user_groups, 'trucks': curr_trucks, 'fuel_t': FUEL_TYPE, 'truck_t': TRUCK_TYPE}
    return render(request, "application/trucks.html", context=context)


@allowed_users(allowed_roles=['client'])
@login_required(login_url='login')
def create_request(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    transport_request = Request()
    client = request.user.username.__str__()
    freight_types = TYPE_FREIGHT
    registration_date = datetime.date.today()
    max_price = 0
    source = ''
    destination = ''
    arrival_date = None
    weight = 0

    if request.method == 'POST':
        transport_request.clientID = request.user
        transport_request.source = request.POST.get('source')
        transport_request.destination = request.POST.get('destination')
        transport_request.freight_type = request.POST.get('freight_types')
        transport_request.arrival_date = request.POST.get('arrival_date')
        transport_request.max_price = request.POST.get('max_price')
        transport_request.weight = request.POST.get('weight')
        transport_request.registration_date = date.today()
        transport_request.save()

    context = {'user_groups': user_groups, 'client': client, 'freight_types': freight_types,
               'registration_date': registration_date, 'max_price': max_price, 'source': source,
               'destination': destination, 'arrival_date': arrival_date, 'weight': weight}

    return render(request, "application/create_request.html", context)


@allowed_users(allowed_roles=['client'])
@login_required(login_url='login')
def offers(request):
    context = create_context(request)
    users = User.objects.all()
    offers = Offer.objects.all()
    trucks = Truck.objects.all()
    context['users'] = users
    context['offers'] = offers
    context['trucks'] = trucks
    return render(request, "application/offers.html", context)


@allowed_users(allowed_roles=['transportator'])
@login_required(login_url='login')
def requests(request):
    context = create_context(request)
    users = User.objects.all()
    requests = Request.objects.all()
    context['users'] = users
    context['requests'] = requests
    return render(request, "application/requests.html", context)
