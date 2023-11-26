from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp import views
from mainapp.apps import MainappConfig
from mainapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    toggle_publish

app_name = MainappConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', cache_page(30)(views.contacts), name='contacts'),
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', cache_page(30)(ProductDetailView.as_view()), name='detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('toggle/<int:pk>/', toggle_publish, name='toggle'),
]