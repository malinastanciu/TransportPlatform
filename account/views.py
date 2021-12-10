from django.shortcuts import render
from django.http import HttpResponse
from arcgis.gis import GIS
from IPython.display import display

# Create your views here.
def home(request):
    gis = GIS()
    map = gis.map("Palm Springs, CA")
    return render(request, 'account/home.html', {'map': map})
