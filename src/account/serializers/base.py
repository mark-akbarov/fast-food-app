from rest_framework import serializers

from account.models.account import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'phone_number',
            'email',
            'role',
            'profile_picture',
            ]
