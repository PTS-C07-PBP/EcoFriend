from django import forms
 
# creating a form
class leadForm(forms.Form):
    forms.CharField(label = "Add Quote")