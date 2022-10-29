from django import forms

class userWeight(forms.Form):
    weight = forms.FloatField(label="Body weight in pounds")