from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

from django import forms
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdate(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

class ProfileUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']