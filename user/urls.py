from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('show_notes/', show_notes, name='show_notes'),
    path('add_notes/', add_notes, name='add_notes'),
    path('add_notes/json', add_notes_json, name='add_notes_json'),
]