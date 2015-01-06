from django import forms

from .models import Pin

class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ('pin_latitude', 'pin_longitude', 'category', 'comment',)
