from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import DisplayMenuView

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', DisplayMenuView.as_view(), name='orders'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),  # New
    path('my-orders/', views.order_tracking, name='order_tracking'),  # Changed path
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.delete_account, name='delete_account'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='orders/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
]