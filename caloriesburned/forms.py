from django import forms

class userWeight(forms.Form):
    weight = forms.FloatField(label="Body weight in pounds")

class addMotive(forms.Form):
    motive = forms.CharField(label="Add new motive")