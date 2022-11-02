from email.policy import default
from tokenize import group
from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import User, Group
from tracker.models import Footprint
from django.dispatch import receiver
from django.db.models.signals import post_save


# class EcoUser(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=User(), unique=True)
#     # id = models.CharField(max_length=5,primary_key=True)
#     email = models.EmailField(max_length=255, null=True, blank=True)
#     username = models.CharField(max_length=20, null=True, blank=True)
#     first_name = models.CharField(max_length=20, null=True, blank=True)
#     last_name = models.CharField(max_length=20, null=True, blank=True)
#     user_role = models.CharField(max_length=20, null=True, blank=True)
#     calories = models.FloatField(null=True, blank=True)
#     carbon = models.FloatField(null=True, blank=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['username','first_name','last_name','user_role']

#     @receiver(post_save, sender=User)
#     def create_user(sender, instance, created, **kwargs):
#         if created:
#             EcoUser.objects.create(user=instance)
    
#     @receiver(post_save, sender=User)
#     def save_user(sender, instance, **kwargs):
#         instance.ecouser.save()

