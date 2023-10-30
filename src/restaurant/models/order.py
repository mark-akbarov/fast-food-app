from django.db import models
from django.contrib.gis.db.models import PointField

from core.utils.base_model import BaseModel
from .dish import Dish
from .restaurant import Restaurant


class OrderStatus(models.TextChoices):
    ACCEPTED = 'accepted'
    CANCELED = 'canceled'
    PENDING = 'pending'
    DELIVERED = 'delivered'


class Order(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=15, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    delivery_address = PointField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    
    def __str__(self) -> str:
        return f"{self.user} -> {self.created_at}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dishes')
    quantity = models.PositiveIntegerField(default=1)

