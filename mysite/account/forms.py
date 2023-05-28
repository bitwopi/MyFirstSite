from django import forms
from account.models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']

