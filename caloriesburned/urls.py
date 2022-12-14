from pyexpat import version_info
from django import views
from django.urls import path
from caloriesburned.views import show_caloriesburned, show_json, show_result, calories_chart, add_motive, get_motive
from caloriesburned.views import get_last_submit, show_json_person, show_json_person_detail, add_person


app_name = 'caloriesburned'

urlpatterns = [
    path('', show_caloriesburned, name='show_caloriesburned'),
    path('show_result/', show_result, name="show_result"),
    path('calories_chart/', calories_chart, name="calories_chart"),
    path('show_json/', show_json, name="show_json"),
    path('show_json_person/', show_json_person, name="show_json_person"),
    path('show_json_person_detail/', show_json_person_detail, name="show_json_person_detail"),
    path('add_motive/', add_motive, name="add_motive"),
    path('add_person/', add_person, name="add_person"),
    path('get_motive/', get_motive, name="get_motive"),
    path('get_last_submit/', get_last_submit, name="get_last_submit"),
]