from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from django.urls import reverse
from custom_users.forms import RegistrationForm,LoginForm


class Registration(CreateView):
    form_class = RegistrationForm
    success_url = '/users/'
    template_name = 'custom_user/register.html'


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = 'custom_user/login.html'

    def get_success_url(self):
        return reverse("users:user_list")


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'custom_user/user_list.html'

    def get_queryset(self):
        return User.objects.all()
