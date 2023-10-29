from geopy.distance import geodesic

DISH_PREPATION_TIME = 5
DURATION_PER_ONE_KILOMETER = 3

def calculate_estimated_delivery_time(dishes, restaurant_location, customer_location) -> int:
    preparation_time = len(dishes) * DISH_PREPATION_TIME
    
    distance = geodesic(restaurant_location, customer_location).kilometers
    print(distance)    
    delivery_time = distance * DURATION_PER_ONE_KILOMETER

    return int(preparation_time + delivery_time)
