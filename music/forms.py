from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate,logout,login,get_user_model





class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


