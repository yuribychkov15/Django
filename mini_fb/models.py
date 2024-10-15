from django.db import models
from django.utils import timezone

from django.urls import reverse

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
        return f'{self.first_name} {self.last_name} {self.city} {self.email}'
    
    def get_status_messages(self):
        '''Return all status messages for this profile'''
        return StatusMessage.objects.filter(profile=self).order_by('-timestamp')
    
    def get_absolute_url(self):
        '''Return a URL to display this profile'''
        return reverse('show_profile', kwargs={'pk': self.pk})
    
class StatusMessage(models.Model):
    ''' Encapsulate the idea of one Status Message '''
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(default=timezone.now)
    # model the 1 to many relationship with Profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the object'''
        return f'{self.message} {self.timestamp} {self.profile}'