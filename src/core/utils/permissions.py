from rest_framework.permissions import BasePermission

from account.models.account import UserRole

    
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'HEAD', 'OPTIONS']
    
    
class ReadWrite(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'POST']
    

class ReadWriteUpdate(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST']


class ReadWriteUpdateDelete(BasePermission):
    def has_permission(self, request, view):
        return True