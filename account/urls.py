from django.contrib import admin
from django.urls import path
from account import views as account_views

urlpatterns = [
    path('register/', account_views.registerPage, name='register'),
    path('login/', account_views.loginPage, name='login'),
    path('logout/', account_views.loginPage, name='login'),
]
