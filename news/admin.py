from django.contrib import admin
from .models import Article
from .forms import ArticleForm

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
admin.site.register(Article, ArticleAdmin)