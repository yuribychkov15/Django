# blog/models.py
# Define the data objects for our application
from django.db import models

# Create your models here.

class Article(models.Model):
    ''' Encapsulate the idea of one Article by some author '''

    # data attributes of an Article:
    # only do python manage.py make migrations <app> and python manage.py migrate when you add data attributes
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of the object'''
        return f'{self.title} by {self.author}'