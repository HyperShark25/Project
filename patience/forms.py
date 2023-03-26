from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(UserCreationForm):
    username = forms.CharField(max_length=50, help_text="")
    email = forms.EmailField(max_length=50, help_text="")
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
