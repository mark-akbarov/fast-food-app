from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from account.serializers.base import UserSerializer
from account.models.account import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    
    def get_permissions(self):
        return super().get_permissions()