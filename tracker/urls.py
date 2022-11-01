from django.urls import path
from tracker.views import add_footprint, show_history, tracker

app_name = 'tracker'

urlpatterns = [
    path('', tracker, name='index'),
    path('get_data', show_history, name='show_history'),
    path('create_data', add_footprint, name='add_footprint'),
]