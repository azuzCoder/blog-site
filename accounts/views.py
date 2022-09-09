from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from .models import CustomUser


class HomePageView(ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = 'index.html'


class RegistrationPageView(CreateView):
    model = CustomUser
    template_name = 'registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:home')


class CustomLoginView(LoginView):
    template_name = 'login.html'