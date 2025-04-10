# orders/urls.py

from django.urls import path
from . import views  # Import your app’s views

# Define URL patterns specific to the 'orders' app
urlpatterns = [
    path('', views.index, name='index'),  # Home page of the orders app
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('main-dishes/', views.main_dishes, name='main_dishes'),
    path('rice-curry-comforts/', views.rice_curry_comforts, name='rice_curry_comforts'),
    path('sandwiches-wraps/', views.sandwiches_wraps, name='sandwiches_wraps'),
    path('sides-snacks/', views.sides_snacks, name='sides_snacks'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_view, name='menu'), 
]

