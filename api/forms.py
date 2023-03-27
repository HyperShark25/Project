from .models import Device
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, help_text="")
    email = forms.EmailField(max_length=50, help_text="")
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mohamed's Form"}),
        #     'topic': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your story'}),
        #     'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Your username'}),
        #     'serial_number': forms.PasswordInput(attrs={'class': 'form-control', 'placehoder': 'Your ID Number'}),
        #     'option2': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Like or Dislike'})
        # }
