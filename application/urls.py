from django.contrib import admin
from django.urls import path
from application import views as application_views

urlpatterns = [
    path('', application_views.home, name='home'),
    path('account/', application_views.account, name='account'),
    path('createoffer/', application_views.offer_view, name='create_offer'),
    path('trucks/', application_views.trucks, name='trucks'),
    path('createrequest/', application_views.create_request, name='create_request'),
    path('administration/', application_views.administration, name='administration'),
    path('administration/updated-user-information/<str:pk>', application_views.update_user_information,
         name='update_user_information')
]
