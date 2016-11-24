'''Models for the frijay app are created here. '''
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''Links UserProfile to a User model instance.'''
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        '''Return username of the user'''
        return self.user.username


class Event(models.Model):
    '''A model for event attended by users'''
    title = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        '''Makes the string representation
        equal to the title of the Event'''
        return self.title
