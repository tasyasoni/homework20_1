from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
]