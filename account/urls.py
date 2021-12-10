from django.contrib import admin
from django.urls import path
from account import views as account_views

urlpatterns = [
    path('', account_views.home, name='home'),
]
