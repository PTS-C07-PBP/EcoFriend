from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    user_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)