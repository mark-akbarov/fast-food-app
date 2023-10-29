from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models.account import UserRole
from core.utils.permissions import ReadOnly
from restaurant.models import Restaurant, Dish
from restaurant.serializers.restaurant import RestaurantSerializer
from restaurant.serializers.dish import DishSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        anonymous_user = self.request.user.is_anonymous
        if anonymous_user or self.request.user.role != UserRole.ADMIN:
            self.permission_classes = [ReadOnly]
        return super().get_permissions()


class RestaurantWithMenuAPIView(APIView):
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        dishes = Dish.objects.filter(restaurant=restaurant)
        return Response(
            {
                "restaurant": RestaurantSerializer(restaurant).data, 
                "menu": [DishSerializer(i).data for i in dishes]
                }
            )
