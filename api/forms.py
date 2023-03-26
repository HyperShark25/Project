from .models import Device
from django import forms


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
