from django.db import models
from django.contrib.gis.db.models import PointField

from core.utils.base_model import BaseModel
from .dish import Dish
from .restaurant import Restaurant


class OrderStatus(models.TextChoices):
    ACCEPTED = 'accepted'
    CANCELED = 'canceled'
    PENDING = 'pending'
    

class Order(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=15, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    delivery_address = PointField()
    dishes = models.ManyToManyField(Dish)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    
    def __str__(self) -> str:
        return f"{self.user} -> {self.created_at}"
