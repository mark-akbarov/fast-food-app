from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from account.models.account import User


def login(username: str, password, is_superuser=False):
    try:
        if username and User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
        else:
            user = User.objects.get(username=username)
        if user.is_active is False:
            return Response(
                {
                    "type": "E_UNACTIVATED_ACCOUNT", 
                    "message": "Account not activated."
                    }, 
                status=status.HTTP_400_BAD_REQUEST
                )
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return Response(
                {
                    "type": "E_INVALID_USERNAME_OR_PASSWORD", 
                    "message": "Username or password is invalid."
                    }, 
                status=status.HTTP_400_BAD_REQUEST
                )
        if is_superuser is True and user.is_superuser is False:
            return Response({'detail': 'access denied'}, status=status.HTTP_400_BAD_REQUEST)
        token = RefreshToken.for_user(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(
            {
                "type": "E_INVALID_USERNAME_OR_PASSWORD", 
                "message": "Username or password is invalid."}, 
            status=status.HTTP_400_BAD_REQUEST
            )
