'''Models for the frijay app are created here. '''
from django.db import models


class User(models.Model):
    '''A model for users of frijay'''
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=60)

    def __str__(self):
        '''Makes the string representation
        equal to the first and last name of the user'''
        return self.first_name + self.last_name


class Event(models.Model):
    '''A model for event attended by users'''
    title = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    address =  models.CharField(max_length=200, null=True)
    host = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    openSeats = models.IntegerField(null=True)
    additionalDetails = models.TextField(blank=True, null=True)

    def __str__(self):
        '''Makes the string representation
        equal to the title of the Event'''
        return self.title
