from django.urls import path
from caloriesburned.views import show_caloriesburned, login_user

app_name = 'caloriesburned'

urlpatterns = [
    path('', show_caloriesburned, name='show_caloriesburned'),
    path('login/', login_user, name='login'),
]