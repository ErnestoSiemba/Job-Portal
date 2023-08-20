from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Username',
            'class': 'text'

        })
        
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Email',
            'class': 'text email'

        })
        
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'Password',
            'class': 'text'

        })
        
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'Confirm Password',
            'class': 'text w3lpass'

        })
        
        
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError('Username cannot be less than 6 characters')
        return username
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Username',
            'class': 'text'

        })
        self.fields['password'].widget.attrs.update({
            'required': '',
            'name': 'password',
            'id': 'password',
            'type': 'password',
            'placeholder': 'Password',
            'class': 'text w3lpass'
        })
        
        # class Meta:
        #     model = User
        #     fields = ['username', 'password']