from django import forms
from .models import Footprint

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Footprint
        fields = ['mileage']