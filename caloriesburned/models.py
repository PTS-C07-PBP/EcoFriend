from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from tracker.models import Footprint
# Create your models here.
class Calories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caloriesBefore = models.FloatField
    caloriesNow = models.FloatField
    caloriesTotal = models.FloatField
