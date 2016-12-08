'''Testing forms'''
# from datetime import datetime, timedelta
# from django import forms
# from django.contrib.auth.models import User
from django.test import TestCase
from frijay.forms import UserForm, EventForm

"""Testing the two forms with input data"""


class FormsTest(TestCase):

    """Testing the event form by filling form with data"""

    def test_valid_data_user(self):
        form = UserForm({
            'first_name': "Avi",
            'last_name': "Kirschenbaum",
            'username': "Avi123",
            'email': "avikirschenbaum@gmail.com",
            'password': "ABC123"
        })
        self.assertTrue(form.is_valid())
        check = form.save()
        self.assertEqual(check.first_name, "Avi")
        self.assertEqual(check.last_name, "Kirschenbaum")
        self.assertEqual(check.username, "Avi123")
        self.assertEqual(check.email, "avikirschenbaum@gmail.com")
        self.assertEqual(check.password, "ABC123")

    '''Testing the event form by filling form with data'''
    def test_valid_data_event(self):
        form = EventForm({
            'title': "Shabbat Table",
            'address': "545 Washington Ave",
            'address2': "APT 100",
            'city': "Brooklyn",
            'state': "New York",
            'zipcode': 11238,
            'phone': 9174741941,
            'date': "2016-12-14",
            'time1': "19:30:00",
            'time2': "22:00:00",
            'openSeats': 5,
            'additionalDetails': "No"
        })
        self.assertTrue(form.is_valid())
        check2 = form.save()
        self.assertEqual(check2.title, "Shabbat Table")
        self.assertEqual(check2.address, "545 Washington Ave")
        self.assertEqual(check2.address2, "APT 100")
        self.assertEqual(check2.city, "Brooklyn")
        self.assertEqual(check2.state, "New York")
        self.assertEqual(check2.zipcode, '11238')
        self.assertEqual(check2.phone, 9174741941)
        self.assertEqual(check2.date.strftime("%Y, %m, %d"), "2016, 12, 14")
        self.assertEqual(check2.time1.strftime("%H:%M:%S"), "19:30:00")
        self.assertEqual(check2.time2.strftime("%H:%M:%S"), "22:00:00")
        self.assertEqual(check2.openSeats, 5)
        self.assertEqual(check2.additionalDetails, "No")
