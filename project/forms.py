# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    ''' Our form to register a new user '''
    password = forms.CharField(widget=forms.PasswordInput)
    favorite_genre = forms.CharField(max_length=100)
    favorite_game = forms.CharField(max_length=100)
    first_game_played = forms.CharField(max_length=100)
    gaming_platform_preference = forms.CharField(max_length=100)
    gaming_goals = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    ''' fields for an individual profile '''
    class Meta:
        model = Profile
        fields = ['favorite_genre', 'favorite_game', 'first_game_played', 'gaming_platform_preference', 'gaming_goals']