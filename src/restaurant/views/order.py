from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models.account import UserRole
from core.utils.permissions import ReadOnly, ReadWrite, ReadWriteUpdateDelete
from restaurant.models import Order
from restaurant.serializers.order import OrderSerializer
from restaurant.models.order import OrderStatus
from restaurant.utils.calculate_distance import calculate_estimated_delivery_time


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_permissions(self):
        """custom permissions for each user"""
        anonymous_user = self.request.user.is_anonymous
        if anonymous_user:
            self.permission_classes = [ReadOnly]
        elif self.request.user.role == UserRole.CUSTOMER:
            self.permission_classes = [ReadWrite]
        else:
            self.permission_classes = [ReadWriteUpdateDelete]
        return super().get_permissions()
    
    def get_queryset(self):
        """custom permissions for each user"""
        anonymous_user = self.request.user.is_anonymous
        if self.request.user.role in [UserRole.ADMIN, UserRole.WAITER]:
            return Order.objects.all().order_by('-created_at')
        elif anonymous_user or self.request.user.role == UserRole.CUSTOMER:
            return Order.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class MyOrdersAPIView(APIView):
    def get(self, request, *args, **kwargs):
            order = Order.objects.filter(user=request.user).last()
            previous_orders_dishes = Order.objects.exclude(id=order.id).filter(status=OrderStatus.ACCEPTED)
            previous_orders = sum([j.quantity for i in previous_orders_dishes for j in i.items.all()])
            dishes = sum([i.quantity for i in order.items.all()])
            if order.status == OrderStatus.PENDING:
                return Response({"detail": "Waiting for restaurant to approve your order."})
            elif order.status == OrderStatus.ACCEPTED:
                res = calculate_estimated_delivery_time(
                    dishes=dishes,
                    customer_location=order.delivery_address,
                    restaurant_location=order.restaurant.address,
                    previous_orders=previous_orders
                )
                return Response({"message": f"Your delivery will arrive in {res} minutes"})
            elif order.status == OrderStatus.CANCELED:
                return Response({"detail": "Your order has been cancelled by the restaurant."})
            return Response({"detail": OrderSerializer(order).data})


# sample_post_request_body = {

#         "status": "pending",
#         "delivery_address": "69.321602 41.316046",
#         "restaurant": 1,
#         "items": [
#             {
#                 "dish": {
#                     "id": 1
#                 },
#                 "quantity": 2
#             },
#             {
#                 "dish": {
#                     "id": 2
#                 },
#                 "quantity": 2
#             }
#         ]
#     }
