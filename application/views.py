from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from arcgis.gis import GIS
from IPython.display import display
from application.functions import create_context
from .forms import OfferForm


# Create your views here.
# @login_required(login_url='login')
# def home(request):
#     gis = GIS()
#     map = gis.map("Palm Springs, CA")
#     return render(request, 'application/home.html', {'map': map})

@login_required(login_url='login')
def home(request):
    context = create_context(request)
    return render(request, 'application/home.html', context)


@login_required(login_url='login')
def account(request):
    context = create_context(request)
    return render(request, 'application/account.html', context)


def offer_view(request):
    context = create_context(request)
    context['form'] = OfferForm()
    return render(request, "application/create_offer.html", context)
