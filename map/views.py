import geopy
from arcgis import GIS
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from geopy import Nominatim

from application.functions import create_context
from application.models import Contract

geopy.geocoders.options.default_user_agent = "map"

@login_required(login_url='login')
def display_map(request, pk):
    context = create_context(request)
    contract = Contract.objects.get(id=pk)
    geolocator1 = Nominatim()
    geolocator2 = Nominatim()
    source = geolocator1.geocode(contract.source)
    destination = geolocator2.geocode(contract.destination)
    context['source_lat'] = source.latitude
    context['source_long'] = source.longitude
    context['destination_lat'] = destination.latitude
    context['destination_long'] = destination.longitude
    context['source'] = source
    context['destination'] = destination
    return render(request, 'map/display_map.html', context)
