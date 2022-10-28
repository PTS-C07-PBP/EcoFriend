from django.forms import ModelForm, Textarea
from review.models import Review

class NewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description', 'rating']
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 15})
        }