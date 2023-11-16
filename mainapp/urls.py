from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig
from mainapp.views import ProductListView, ProductDetailView, ProductCreateView

app_name = MainappConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
]