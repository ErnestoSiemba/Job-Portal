from django import forms
from django.contrib.auth.forms import UserChangeForm
from account.models import User

class UserProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required': '',
            'name': 'firstname',
            'id': 'firstname',
            'type': 'text',
            'placeholder': 'First Name',
            'class': 'text'

        })
        self.fields['last_name'].widget.attrs.update({
            'required': '',
            'name': 'lastname',
            'id': 'lastname',
            'type': 'text',
            'placeholder': 'Last Name',
            'class': 'text'

        })
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
        self.fields['address'].widget.attrs.update({
            'required': '',
            'name': 'address',
            'id': 'address',
            'type': 'text',
            'placeholder': 'Address',
            'class': 'text'

        })
        self.fields['location'].widget.attrs.update({
            'required': '',
            'name': 'location',
            'id': 'location',
            'type': 'text',
            'placeholder': 'Location',
            'class': 'text'

        })
    
    username = forms.CharField(max_length=100, help_text="")
    address = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'label': 'Address:'}))    
    location = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'label': 'Location:'}))    
    gender = forms.ChoiceField(choices=User.GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'location', 'gender', 'profile_picture']
        