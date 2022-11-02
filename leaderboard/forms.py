from django import forms
 
# creating a form
class CommentForm(forms.Form):
    comment = forms.CharField(label='Enter Your Comment Here', max_length=200, required=True)
