from restaurant.models.order import Order, OrderStatus
from .calculate_distance import calculate_estimated_delivery_time


def create_order_for_customer(
    user, 
    restaurant, 
    dishes, 
    delivery_address, 
    customer_address
    ):
    order = Order.objects.create(
        user=user, 
        restaurant=restaurant, 
        dishes=dishes, 
        delivery_address=delivery_address, 
        customer_address=customer_address
        )
    return order


def process_order(order: Order):
    if order.status == OrderStatus.PENDING:
        return {"detail": "Waiting for restaurant to accept your order"}
    elif order.status == OrderStatus.ACCEPTED:
        return {"detail": "Your order was accepted"}