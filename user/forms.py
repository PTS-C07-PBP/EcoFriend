from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.hashers import make_password

# Form membuat User
class RegistrationForm(UserCreationForm):
    CHOICES=[('admin','Admin'),
         ('ecouser','EcoUser')]
    
    # user_id = forms.IntegerField()
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=20, label="First Name")
    last_name = forms.CharField(max_length=20, label="Last Name")
    user_role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Role")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_role']
    
    # def save(self, commit=True):
        
    #     user = super(UserCreationForm, self).save(commit=False)
        
    #     # print(user)
    #     # # print(user.first_name)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.user_id = self.cleaned_data['user_id']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     user.user_role = self.cleaned_data['user_role']
    #     if commit:
    #         user.save()
    #     print('test')
    #     EcoUser.save(user=user)

        

        # return user


