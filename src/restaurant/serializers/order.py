from rest_framework import serializers

from restaurant.models.order import Order
from restaurant.serializers.restaurant import PointField

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at', ]


class CreateOrderSerializer(serializers.ModelSerializer):
    delivery_address = PointField()
    
    class Meta:
        model = Order
        fields = [
            'dishes',
            'delivery_address',
            'status',
    
        ]
        extra_kwargs = {
            'status': {'read_only': True}
        }
    