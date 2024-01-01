from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('index',views.index, name="index"),
    path('productos',views.productos, name="Productos"),
    path('Biribir',views.Biribir, name="Biribiri"),
    path('Inake',views.Inake, name="Ina cake"),
    path('Trululu',views.Trululu, name="Trululu"),
    
]
