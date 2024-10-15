from django import forms
from .models import *

class CreateProfileForm(forms.ModelForm):
    # Our form to create a profile
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email', 'image_url']

class CreateStatusMessageForm(forms.ModelForm):
    # Our form to create a status message
    class Meta:
        model = StatusMessage
        fields = ['message']