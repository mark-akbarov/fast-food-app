from geopy.distance import geodesic


DISH_PREPATION_TIME = 5
DURATION_PER_ONE_KILOMETER = 3


def calculate_estimated_delivery_time(dishes, restaurant_location, customer_location, previous_orders=0) -> int:
    previous_orders * DISH_PREPATION_TIME
    
    preparation_time = dishes * DISH_PREPATION_TIME
    
    distance = geodesic(restaurant_location, customer_location).kilometers
   
    delivery_time = distance * DURATION_PER_ONE_KILOMETER

    return int(preparation_time + delivery_time + previous_orders)
