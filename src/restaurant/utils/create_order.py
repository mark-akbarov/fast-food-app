from restaurant.models.order import Order


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