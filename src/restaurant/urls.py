from django.urls import include, path

from rest_framework.routers import DefaultRouter

from restaurant.views.restaurant import RestaurantViewSet, RestaurantWithMenuAPIView
from restaurant.views.dish import DishViewSet
from restaurant.views.order import OrderViewSet, MyOrdersAPIView

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('dishes', DishViewSet,  basename='dishes')
router.register('orders', OrderViewSet, basename='orders')


urlpatterns = [
    path('', include(router.urls)),
    path('restaurants/<int:pk>/dishes/', RestaurantWithMenuAPIView.as_view(), name='restaurant-with-menu'),
    # path('restaurants/<int:pk>/orders/create/', CreateOrderAPIView.as_view(), name='create-order-for-customer'),
    path('my-orders/', MyOrdersAPIView.as_view(), name='my-orders')
]