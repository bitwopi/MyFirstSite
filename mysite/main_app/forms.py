from django import  forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': "form-control"
        })
        self.fields['password2'].widget.attrs.update({
            'class': "form-control"
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control",
                                                'id': "floatingInput"}),
            'email': forms.EmailInput(attrs={'class': "form-control",
                                            'id': "floatingEmail"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': "form-control",
                                                                               'id': "floatingInput"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control",
                                                                                   'id': "floatingPassword"}))


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'
