from django import forms
from django.contrib.auth.models import User
from .models import Pin, UserProfile


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ('pin_latitude', 'pin_longitude', 'category', 'comment',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

