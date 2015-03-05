from django import forms
from django.contrib.auth.models import User
from .models import Pin, UserProfile, Map
from django.shortcuts import get_object_or_404, redirect


class PinForm(forms.ModelForm):
    Map = forms.ModelChoiceField(queryset=Map.objects.all().order_by('map_title'))

    class Meta:
        model = Pin
        fields = ('category', 'comment',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class MapCenterForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ('map_title',)
        labels = {'map_title': ('Enter a Title for your Trip'), }

    country = forms.CharField(label = 'Enter the country you are travelling to', max_length=255)

class PinSearchForm(forms.Form):
    address = forms.CharField(label = 'Enter Pin Location', max_length=255)
    
