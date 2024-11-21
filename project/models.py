from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

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
    # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
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