from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='project_profile')
    profile_image = models.ImageField(upload_to='profile_images/')
    favorite_genre = models.CharField(max_length=100)
    favorite_game = models.CharField(max_length=100)
    first_game_played = models.CharField(max_length=100)
    gaming_platform_preference = models.CharField(max_length=100)
    gaming_goals = models.TextField()

    def get_absolute_url(self):
        '''Return a URL to display this profile'''
        return reverse('show_profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username

class Game(models.Model):
    ''' Encapsulates the model for an individual game '''
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='game_covers/')

    def __str__(self):
        return self.title

class Review(models.Model):
    ''' Encapsulates the model for our reviews '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    review_text = models.TextField()
    review_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} for {self.game.title}"

class Collection(models.Model):
    ''' Encapsulates the model for our game collection for each user '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Collection Item: {self.game.title}"