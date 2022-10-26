from django.urls import path

from tracker.views import add_footprint, show_history, tracker, login_user, logout_user, register

app_name = 'tracker'

# urlpatterns = [
#     path('', tracker_submit, name='tracker_submit'),
# ]

urlpatterns = [
    path('', tracker, name='index'),
    path('get_data', show_history, name='show_history'),
    path('create_data', add_footprint, name='add_footprint'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]