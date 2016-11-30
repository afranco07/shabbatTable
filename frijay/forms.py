from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta
from frijay.models import UserProfile, Event


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
    # password2 = forms.CharField(
    #     label=("Confirm Password *"),
    #     widget=forms.PasswordInput(attrs=dict(required=True,
    #                                           max_length=30,
    #                                           render_value=False)))

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(
                "This email is already used with an account.")
        return data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class EventForm(forms.ModelForm):
    """ Form to Host a Dinner """
    title = forms.CharField(
        max_length=128, help_text="Please enter a title.")
    address = forms.CharField(
        max_length=160, help_text="Please enter the address.")
    # host = forms.CharField(widget=forms.HiddenInput())
    date = forms.DateField(initial=datetime.today().date() + timedelta(days=7))
    time = forms.TimeField(initial=datetime.now().time())
    openSeats = forms.IntegerField(
        initial=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    # additionalDetails = forms.CharField(max_length=160)
    class Meta:
        model = Event
        fields = ('title',
                  'address',
                  'date',
                  'time',
                  'openSeats',
                  'additionalDetails')
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(EventForm, self).__init__(*args, **kwargs)
    # def clean_username(self):
    #     return self.user.username
