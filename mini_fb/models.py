from django.db import models

# Create your models here.

class Profile(models.Model):
    ''' Encapsulate the idea of one Profile '''

    # data attributes of an Article:
    # only do python manage.py make migrations <app> and python manage.py migrate when you add data attributes
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of the object'''
        return f'{self.first_name} {self.last_name}'