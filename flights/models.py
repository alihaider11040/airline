from django.db import models

# Create your models here.




class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)



class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name='departure')
    destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name='destination')
    duration = models.IntegerField()