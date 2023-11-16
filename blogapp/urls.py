from django.urls import path

from blogapp import views
from blogapp.apps import BlogappConfig
from blogapp.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_publish

app_name = BlogappConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('toggle/<int:pk>/', toggle_publish, name='toggle'),
]