from django.contrib import admin
from django.urls import path
from map import views as map_views

urlpatterns = [
    path('contract/view-map/<str:pk>',  map_views.display_map, name='display_map'),

]
