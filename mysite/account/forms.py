from django import forms
from account.models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_field = {'class': "form-control"}
        self.fields['username'].widget.attrs.update(class_field)
        self.fields['email'].widget.attrs.update(class_field)
        self.fields['avatar'].widget.attrs.update(class_field)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']

