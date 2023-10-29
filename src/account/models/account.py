import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    WAITER = 'waiter'
    CUSTOMER = 'customer'

  
class User(AbstractUser):
    username = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    phone_number = models.CharField(max_length=12, null=True, unique=True)
    email = models.EmailField(max_length=255, null=True, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    profile_picture = models.ImageField(upload_to='user', help_text='User Images', null=True)
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.CUSTOMER)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']
    
    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
