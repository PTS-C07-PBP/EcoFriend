from django.urls import path
from review.views import *
from review.views import show_review_ajax, show_json, add_review

app_name = 'review'

urlpatterns = [
    path('', show_review_ajax, name='show_review_ajax'),
    path('json/', show_json, name="show_json"),
    path('addreview/', add_review, name="add_review"),
]