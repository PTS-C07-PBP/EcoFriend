from django import forms
from . import models

CHOICES = [('all', 'All'), ('africa', 'Africa'), ('middle east', 'Middle East'), ('europe', 'Europe'), ('americas', 'Americas'), ('global', 'Global'), ('asia pacific', 'Asia Pacific')]

# Form membuat artikel
class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'region', 'description']

# Form filter artikel
class FilterForm(forms.Form):
    filter_region = forms.CharField(label="Filter based on region", widget=forms.Select(choices=CHOICES))