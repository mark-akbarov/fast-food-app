from rest_framework import serializers

from restaurant.serializers.restaurant import PointField
from restaurant.models import Order, OrderItem, Dish


class DishIDSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = [
            'id',  
            'price',
            'name',
            'description',
            'restaurant'
            ]


class OrderItemSerializer(serializers.ModelSerializer):
    dish = DishIDSerializer()

    class Meta:
        model = OrderItem
        fields = [
            'id', 
            'dish', 
            'quantity'
            ]

    def create(self, validated_data):
        dish_data = validated_data.pop('dish')
        dish = Dish.objects.get(pk=dish_data['id'])
        order_item = OrderItem.objects.create(dish=dish, **validated_data)
        return order_item
    

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    delivery_address = PointField()

    class Meta:
        model = Order
        fields = [
            'id', 
            'status', 
            'delivery_address', 
            'restaurant', 
            'items'
            ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            dish_data = item_data.pop('dish')
            dish = Dish.objects.get(id=dish_data['id'])
            OrderItem.objects.create(order=order, dish=dish, **item_data)
        return order