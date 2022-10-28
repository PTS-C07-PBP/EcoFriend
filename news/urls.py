from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', news, name='news'),
    path('news/init/', init_articles, name='init_articles'),
    path('news/articles/', show_articles, name='show_articles'),
    path('news/add/', add_article, name='add_article'),
    path('news/delete/<int:id>', delete_article, name='delete_article'),
    path('news/reset/', reset, name='reset'),
    path('news/json/', json, name='json'),
]