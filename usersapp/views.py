from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from usersapp.forms import UserRegisterForm, UserProfileForm
from usersapp.models import User


class LoginView(BaseLoginView):
    model = User
    template_name = 'usersapp/login.html'
    # success_url = reverse_lazy('mainapp:home')

class LogoutView(BaseLogoutView):
    model = User
    # success_url = reverse_lazy('mainapp:home')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'usersapp/register.html'
    success_url = reverse_lazy('usersapp:login')

class ProfileView (UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'usersapp/profile.html'
    success_url = reverse_lazy('mainapp:home')

    def get_object(self, queryset=None):
        return self.request.user

