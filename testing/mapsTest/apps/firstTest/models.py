from django.db import models

class LocationManager(models.Manager):
    def addLocation(self,lat,lng):
        newLoc = Location.objects.create(latitude=lat,longitude=lng)
        return newLoc

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    objects = LocationManager()