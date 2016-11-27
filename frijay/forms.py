from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta
from frijay.models import UserProfile, Event


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class EventForm(forms.ModelForm):
    """ Form to make an Event """
    title = forms.CharField(
        max_length=128, help_text="Please enter a title.")
    address = forms.CharField(
        max_length=160, help_text="Please enter the address.")
    date = forms.DateField(initial=datetime.today().date() + timedelta(days=7))
    time = forms.TimeField(initial=datetime.now().time())
    openSeats = forms.IntegerField(
        initial=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    # additionalDetails = forms.CharField(null=True, max_length=160)
    class Meta:
        model = Event
        fields = (
            'title',
            'address',
            'host',
            'date',
            'time',
            'openSeats',
            'additionalDetails')
