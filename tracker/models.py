from django.db import models
from django.contrib.auth.models import User

class Footprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    mileage = models.FloatField()
    carbon = models.FloatField()
    onFoot = models.BooleanField()