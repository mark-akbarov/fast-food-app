from django.contrib.gis.geos import fromstr

from rest_framework import serializers

from restaurant.models.restaurant import Restaurant


class PointField(serializers.Field):
    def to_representation(self, value):
        return (f"{value.x} {value.y}")

    def to_internal_value(self, data):
        longitude, latitude = data.split()
        return fromstr(f'POINT({longitude} {latitude})')
        

class RestaurantSerializer(serializers.ModelSerializer):
    address = PointField()
    
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'open_time',
            'close_time',
            'address'
        ]
