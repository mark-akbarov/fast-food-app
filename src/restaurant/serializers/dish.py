from rest_framework import serializers

from restaurant.models.dish import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ['created_at', 'updated_at', ]
