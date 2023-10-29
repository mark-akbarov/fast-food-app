from django.contrib import admin

from restaurant.models.restaurant import Restaurant
from restaurant.models.order import Order
from restaurant.models.dish import Dish

admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Dish)
