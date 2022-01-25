from django.contrib import admin
from django.urls import path
from application import views as application_views

urlpatterns = [
    path('', application_views.home, name='home'),
    path('account/', application_views.account, name='account'),
    path('createoffer/', application_views.offer_view, name='create_offer'),
    path('trucks/', application_views.trucks, name='trucks'),
    path('createrequest/', application_views.create_request, name='create_request'),
    path('offers/', application_views.offers, name='offers'),
    path('requests/', application_views.requests, name='requests'),
    path('admin/', application_views.administrator, name='admin'),
    path('contracts/', application_views.contracts, name='contracts'),
    path('generate-contract-for-offer/<str:pk>', application_views.generate_contract_for_offer,
         name='generate_contract_for_offer'),
    path('generate-contract-for-request/<str:pk>', application_views.generate_contract_for_request,
         name='generate_contract_for_request'),
    path('delete_offer/<str:pk>', application_views.delete_offer, name='delete_offer'),
    path('delete_request/<str:pk>', application_views.delete_request, name='delete_request'),
]
