from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', news, name='news'),
    path('init/', init_articles, name='init_articles'),
    path('articles/', show_articles, name='show_articles'),
    path('add/', add_article, name='add_article'),
    path('delete/<int:id>', delete_article, name='delete_article'),
    path('json/', json, name='json'),
]