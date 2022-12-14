from django.db import models
from datetime import date
from django.contrib.auth.models import User

CHOICES = [('global', 'Global'), ('africa', 'Africa'), ('middle east', 'Middle East'), ('europe', 'Europe'), ('americas', 'Americas'), ('asia pacific', 'Asia Pacific')]
# Model untuk article
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    admin_created = models.BooleanField(default=False)
    image = models.URLField()
    link = models.URLField()
    title = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    region = models.CharField(max_length=255, choices=CHOICES, default='Global')
    description = models.TextField()

