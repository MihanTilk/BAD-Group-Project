# orders/urls.py

from django.urls import path
from . import views  # Import your app’s views

# Define URL patterns specific to the 'orders' app
urlpatterns = [
    path('', views.index, name='index'),  # Home page of the orders app
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('main-dishes/', views.main_dishes, name='main_dishes'),
]

