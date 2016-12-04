"""Forms for the project are created here"""
from datetime import datetime, timedelta
from django import forms
from django.contrib.auth.models import User
from frijay.models import Event


class UserForm(forms.ModelForm):
    """ Registration Form to register a new User """
    first_name = forms.CharField(label="First Name *", required=True)
    last_name = forms.CharField(label="Last Name *", required=True)
    username = forms.RegexField(
        label="Username *",
        max_length=30,
        regex=r'^[\w]+$',
        required=True,
        error_messages={'invalid':
                            "May contain only letters, numbers and _ characters."})
    email = forms.EmailField(
        label=("Email address *"),
        widget=forms.TextInput(attrs=dict(unique=True,
                                          required=True,
                                          max_length=30)))
    password = forms.CharField(
        label=("Password *"),
        widget=forms.PasswordInput(attrs=dict(required=True,
                                              max_length=30,
                                              render_value=False)))

    class Meta:
        """Connects UserForm to the built-in model User"""
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password')

    def clean_email(self):
        '''Cleans email address input'''
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(
                "This email is already used with an account.")
        return data


class EventForm(forms.ModelForm):
    """ Form to Host a Dinner. Host name selected in the views. """
    title = forms.CharField(label="Title *",
                            widget=forms.TextInput(attrs={'required': True, 'max_length': 30}))
    # Street Address, Line 1
    address = forms.CharField(label="Street Address *",
                              required=True,
                              max_length=160,
                              help_text="Please enter the address.")
    # Street Address, Line 2
    address2 = forms.CharField(label="Apt / Floor *", max_length=40)
    city = forms.CharField(label="City *", required=True, max_length=15)
    state = forms.CharField(label="State *", required=True, max_length=15)
    zipcode = forms.IntegerField(label="ZIP code *",
                                 min_value=10000,
                                 max_value=99999)
    phone = forms.IntegerField(min_value=1000000000, max_value=9999999999)
    date = forms.DateField(label="Date", initial=datetime.today().date() + timedelta(days=7))
    # Starting time
    time1 = forms.TimeField(label="Starting at", initial=datetime.now().time())
    # Ending time
    time2 = forms.TimeField(label="Ending at", initial=datetime.now().time())
    openSeats = forms.IntegerField(label="Available Seats",
                                   initial=10, min_value=1, max_value=10)
    additionalDetails = forms.CharField(
        label="Details",
        widget=forms.Textarea(attrs=dict(max_length=160)))

    class Meta:
        """Connects EventForm to the model Event"""
        model = Event
        fields = ('title',
                  'address',
                  'address2',
                  'city',
                  'state',
                  'zipcode',
                  'phone',
                  'date',
                  'time1',
                  'time2',
                  'openSeats',
                  'additionalDetails',)
