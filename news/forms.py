from django import forms
from . import models

CHOICES = [('all', 'All'), ('africa', 'Africa'), ('middle east', 'Middle East'), ('europe', 'Europe'), ('americas', 'Americas'), ('global', 'Global'), ('asia pacific', 'Asia Pacific')]

# Form membuat artikel
class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = False

    class Meta:
        model = models.Article
        fields = ['title', 'region', 'description']

# Form filter artikel
class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = False

    filter_region = forms.CharField(label="Region", widget=forms.Select(choices=CHOICES))