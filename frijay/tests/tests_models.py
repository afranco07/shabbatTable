'''Unittests for the frijay app'''
from django.contrib.auth.models import User
from django.test import TestCase
from frijay.models import Event
# from frijay.models import UserProfile


# Create your tests here.
class EventModelTest(TestCase):
    '''Testing the Event Model'''

    def test_string_representation(self):
        '''Test __str__ method for Event'''
        event = Event(title="My title")
        self.assertEqual(str(event), event.title)


# class UserProfileModelTest(TestCase):
#     '''Testing the User Model'''
#
#     def test_string_representation(self):
#         '''Test __str__ method for User'''
#         user = User(first_name='Abraham', last_name='Lincoln', username='mrpresident')
#         userprofile = UserProfile(user=user)
#         self.assertEqual(str(userprofile), userprofile.username)
