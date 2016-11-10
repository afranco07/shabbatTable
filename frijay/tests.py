'''Unittests for the frijay app'''
from django.test import TestCase
from .models import Event
from .models import User

# Create your tests here.
class EventModelTest(TestCase):
    '''Testing the Event Model'''
    def test_string_representation(self):
        '''Test __str__ method for Event'''
        event = Event(title="My title")
        self.assertEqual(str(event), event.title)

class UserModelTest(TestCase):
    '''Testing the User Model'''
    def test_string_representation(self):
        '''Test __str__ method for User'''
        user = User(first_name='Abraham',last_name='Lincoln')
        self.assertEqual(str(user), user.first_name+user.last_name)
