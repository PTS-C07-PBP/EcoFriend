from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]