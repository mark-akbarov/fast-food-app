from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models.account import UserRole
from core.utils.permissions import ReadOnly, ReadWrite, ReadWriteUpdateDelete
from restaurant.models import Order, Restaurant, Dish
from restaurant.serializers.order import OrderSerializer, CreateOrderSerializer
from restaurant.utils import calculate_estimated_delivery_time


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_permissions(self):
        """Set custom permissions for each action."""
        anonymous_user = self.request.user.is_anonymous
        if anonymous_user:
            self.permission_classes = [ReadOnly]
        elif self.request.user.role == UserRole.CUSTOMER:
            self.permission_classes = [ReadWrite]
        else:
            self.permission_classes = [ReadWriteUpdateDelete]
        return super().get_permissions()


class CreateOrderAPIView(APIView):
    def post(self, request, pk, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.create(
            user = request.user, 
            delivery_address=serializer.validated_data['delivery_address'],
            restaurant=restaurant
            )
        ordered_dishes = request.data.get('dishes', [])
        dishes = Dish.objects.filter(pk__in=ordered_dishes)
        order.dishes.set(dishes)
        order.save()
        res = calculate_estimated_delivery_time(
            dishes=dishes,
            customer_location=serializer.validated_data['delivery_address'],
            restaurant_location=restaurant.address
        )
        return Response({"message": f"Your delivery will arrive in {res} minutes"})


{"dishes": [1,2,3], "delivery_address": "69.321602 41.316046"}
