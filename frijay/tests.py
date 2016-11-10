'''Unittests for the frijay app'''
from django.test import TestCase
from .models import Event
from .models import User

# Create your tests here.
class EventModelTest(TestCase):
    '''Testing the Event Model'''
    def test_string_representation(self):
        event = Event(title="Insert title")
        self.assertEqual(str(event), event.title)

class UserModelTest(TestCase):
    '''Testing the User Model'''
    def test_string_representation(self):
        user = User(first_name='Abham',last_name='Lin')
        self.assertEqual(str(user), user.first_name+user.last_name)

    def test_first_name(self):
        user = User(first_name='Fname')
        self.assertEqual(str(user), user.first_name)
