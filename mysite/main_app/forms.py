from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
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


class CreatePostFormAnime(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_field = {'class': "form-control"}
        self.fields['title'].widget.attrs.update(class_field)
        self.fields['synonyms'].widget.attrs.update(class_field)
        self.fields['slug'].widget.attrs.update(class_field)
        self.fields['description'].widget.attrs.update(class_field)
        self.fields['rate'].widget.attrs.update(class_field)
        self.fields['out_date'].widget.attrs.update(class_field)
        self.fields['category'].widget.attrs.update(class_field)
        self.fields['type'].widget.attrs.update(class_field)
        self.fields['episodes_now'].widget.attrs.update(class_field)
        self.fields['episodes_all'].widget.attrs.update(class_field)
        self.fields['duration'].widget.attrs.update(class_field)
        self.fields['studios'].widget.attrs.update(class_field)
        self.fields['persons'].widget.attrs.update(class_field)
        self.fields['main_chars'].widget.attrs.update(class_field)
        self.fields['source'].widget.attrs.update(class_field)

    class Meta:
        model = Anime
        fields = '__all__'


class CreatePostFormManga(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_field = {'class': "form-control"}
        self.fields['title'].widget.attrs.update(class_field)
        self.fields['synonyms'].widget.attrs.update(class_field)
        self.fields['slug'].widget.attrs.update(class_field)
        self.fields['description'].widget.attrs.update(class_field)
        self.fields['rate'].widget.attrs.update(class_field)
        self.fields['release_date'].widget.attrs.update(class_field)
        self.fields['main_characters'].widget.attrs.update(class_field)
        self.fields['category'].widget.attrs.update(class_field)
        self.fields['main_characters'].widget.attrs.update(class_field)
        self.fields['author'].widget.attrs.update(class_field)

    class Meta:
        model = Manga
        fields = '__all__'


class CreatePostFormCharacter(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_field = {'class': "form-control"}
        self.fields['name'].widget.attrs.update(class_field)
        self.fields['synonyms'].widget.attrs.update(class_field)
        self.fields['slug'].widget.attrs.update(class_field)
        self.fields['description'].widget.attrs.update(class_field)
        self.fields['voice_actor'].widget.attrs.update(class_field)

    class Meta:
        model = Character
        fields = '__all__'


class CreatePostFormPerson(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_field = {'class': "form-control"}
        self.fields['name'].widget.attrs.update(class_field)
        self.fields['synonyms'].widget.attrs.update(class_field)
        self.fields['slug'].widget.attrs.update(class_field)
        self.fields['birth_date'].widget.attrs.update(class_field)
        self.fields['career'].widget.attrs.update(class_field)

    class Meta:
        model = Person
        fields = '__all__'


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "form-control",
                                                                           'id': "floatingEmail"}))


class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(
        attrs={'class': "form-control"}))
