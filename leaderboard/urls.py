from django import shortcuts
from django.urls import path

from leaderboard.views import show_leaderboard, show_comment, add_comment

app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard , name = 'show_leaderboard'),
    path('comment/json/', show_comment, name='show_comment'),
    path('comment/add/', add_comment, name='add_comment')
]