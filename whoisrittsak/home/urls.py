from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile'),
]
