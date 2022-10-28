from django.urls import path
from user.views import *

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', user_profile, name='user_profile'),
]