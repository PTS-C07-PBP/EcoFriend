from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField()

class DataCalories(models.Model):
    pemilik = models.ForeignKey(Person, on_delete=models.CASCADE)
    mileage = models.FloatField(default=0)

