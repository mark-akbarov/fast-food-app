from django.db import models
from django.contrib.gis.db.models import PointField

from core.utils.base_model import BaseModel


class Restaurant(BaseModel):
    name = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
    address = PointField()
        
    def __str__(self) -> str:
        return self.name
