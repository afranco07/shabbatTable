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
    title = models.CharField(max_length=80, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    # Street Address, Line 1, required
    address = models.CharField("Street Address", max_length=40)
    address2 = models.CharField("Apt/Floor", max_length=40, null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    zipcode = models.CharField("ZIP code", max_length=5)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField("Date")
    time1 = models.TimeField("From")
    time2 = models.TimeField("Till")
    openSeats = models.IntegerField("Number of Seats Open")
    additionalDetails = models.TextField("Additional Details",
                                         blank=True,
                                         null=True)

    def __str__(self):
        '''Makes the string representation
        equal to the title of the Event'''
        return self.title


class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name
