from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
# Create your forms here.

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'type': 'text',
            'id': 'InputUsername',
            'aria-describedby': 'usernameHelp',
            'placeholder': 'Username',
            'name': 'username',
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'type': 'text',
            'id': 'exampleFirstName',
            'placeholder': 'First Name',
            'name': 'first_name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'type': 'text',
            'id': 'exampleFirstName',
            'placeholder': 'Last Name',
            'name': 'last_name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'type': 'email',
            'id': 'email',
            'aria-describedby': 'emailHelp',
            'placeholder': 'Email Address',
            'name': 'email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'type': 'password',
            'id': 'examplePasswordInput',
            'placeholder': 'Password',
            'name': 'password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'type': 'password',
            'id': 'exampleRepeatPasswordInput',
            'placeholder': 'Repeat Password',
            'name': 'password_repeat',
        })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]



       
