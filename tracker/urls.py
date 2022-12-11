from django.urls import path
from tracker.views import add_footprint, show_json, tracker

app_name = 'tracker'

urlpatterns = [
    path('', tracker, name='index'),
    path('show_json', show_json, name='show_json'),
    path('create_data', add_footprint, name='add_footprint'),
]