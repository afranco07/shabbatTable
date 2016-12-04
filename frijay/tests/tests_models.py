'''Unittests for the frijay app'''
from django.contrib.auth.models import User
from django.test import TestCase
from frijay.models import Event


# Create your tests here.
class EventModelTest(TestCase):
    '''Testing the Event Model'''

    def test_string_representation(self):
        '''Test __str__ method for Event'''
        event = Event(title="My title")
        self.assertEqual(str(event), event.title)
