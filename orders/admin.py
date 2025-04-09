from django.contrib import admin
from .models import FoodItem, Order, OrderItem

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(OrderItem)

