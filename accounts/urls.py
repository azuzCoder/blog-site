from django.urls import path
from .views import HomePageView, RegistrationPageView, CustomLoginView
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', RegistrationPageView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
