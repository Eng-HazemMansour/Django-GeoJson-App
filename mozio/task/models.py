from django.db import models
from django.contrib.gis.db import models
from geojson import Polygon

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumber = models.IntegerField()
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    location = models.PolygonField(geography=True, srid=4326, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def latitude(self):
        if self.location:
            return self.location.y

    @property
    def longitude(self):
        if self.location:
            return self.location.x
    