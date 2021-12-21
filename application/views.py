from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from arcgis.gis import GIS
from IPython.display import display


# Create your views here.
@login_required(login_url='login')
def home(request):
    gis = GIS()
    map = gis.map("Palm Springs, CA")
    return render(request, 'application/home.html', {'map': map})
