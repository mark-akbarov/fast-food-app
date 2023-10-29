from django.db import models
from core.utils.base_model import BaseModel


class Dish(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE, related_name='dishes')
    quantity = models.PositiveIntegerField()
    
    class Meta:
        verbose_name ='Dish'
        verbose_name_plural = 'Dishes'
    
    def __str__(self) -> str:
        return self.name
    
    
