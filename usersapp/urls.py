from django.urls import path
from usersapp.apps import UsersappConfig
from usersapp.views import LoginView, LogoutView, RegisterView, ProfileView

app_name = UsersappConfig.name


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
]