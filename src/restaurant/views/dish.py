from rest_framework.viewsets import ModelViewSet

from account.models.account import UserRole
from core.utils.permissions import ReadOnly, ReadWriteUpdateDelete
from restaurant.models.dish import Dish
from restaurant.serializers.dish import DishSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    
    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.request.user.is_anonymous or self.request.user.role == UserRole.CUSTOMER:
            self.permission_classes = [ReadOnly]
        elif self.request.user.role in [UserRole.WAITER, UserRole.ADMIN]:
            self.permission_classes = [ReadWriteUpdateDelete]
        return super().get_permissions()
