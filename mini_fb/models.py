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
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        '''Return a string representation of the object'''
        return f'{self.first_name} {self.last_name} {self.city} {self.email}'
    
    def get_status_messages(self):
        '''Return all status messages for this profile'''
        return StatusMessage.objects.filter(profile=self).order_by('-timestamp')
    
    def get_absolute_url(self):
        '''Return a URL to display this profile'''
        return reverse('show_profile', kwargs={'pk': self.pk})
    
    def get_friends(self):
        # get the friendships
        friends1 = Friend.objects.filter(profile1=self).values_list('profile2', flat=True)
        friends2 = Friend.objects.filter(profile2=self).values_list('profile1', flat=True)
        # combine both
        friend_ids = set(list(friends1) + list(friends2))
        # get Profile instance
        friends = Profile.objects.filter(id__in=friend_ids)
        return list(friends)
    
class StatusMessage(models.Model):
    ''' Encapsulate the idea of one Status Message '''
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(default=timezone.now)
    # model the 1 to many relationship with Profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the object'''
        return f'{self.message} {self.timestamp} {self.profile}'
    
    def get_images(self):
        return self.images.all()
    
class Image(models.Model):
    ''' Encapsulate the idea of one Image that is not a URL '''
    image_file = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(default=timezone.now)
    status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        '''Return a string representation of the object'''
        return f'{self.image_file} {self.timestamp} {self.status_message}'

class Friend(models.Model):
    profile1 = models.ForeignKey(Profile, related_name='profile1', on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name='profile2', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.profile1.first_name} {self.profile1.last_name} & {self.profile2.first_name} {self.profile2.last_name}"