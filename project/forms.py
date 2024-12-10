# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateProfileForm(forms.ModelForm):
    ''' fields for an individual profile '''
    class Meta:
        model = Profile
        fields = ['profile_image', 'favorite_genre', 'favorite_game', 'first_game_played', 'gaming_platform_preference', 'gaming_goals']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'platform', 'developer', 'release_date', 'cover_image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'review_text']
    
class ReviewFormWithoutGame(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'favorite_genre', 'favorite_game', 'first_game_played', 'gaming_platform_preference', 'gaming_goals']