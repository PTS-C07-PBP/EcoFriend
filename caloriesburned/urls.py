from django.urls import path
from caloriesburned.views import show_caloriesburned, login_user, logout_user, show_result, calories_chart


app_name = 'caloriesburned'

urlpatterns = [
    path('', show_caloriesburned, name='show_caloriesburned'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('show_result/', show_result, name="show_result"),
    path('calories_chart/', calories_chart, name="calories_chart"),
]