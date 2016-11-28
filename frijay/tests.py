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
        self.assertEqual(str(user), user.first_name)

class viewsTest(TestCase):

    '''Test the index.html page'''
    def test_indexPage(self):
        response = self.client.get("/frijay/")
        self.assertEqual(response.status_code, 200)

    '''Test the reservation.html page'''
    def test_reservationPage(self):
        response = self.client.get("/frijay/reservations/")
        self.assertEqual(response.status_code, 200)

    '''Test the events.html page'''
    def test_eventsPage(self):
        response = self.client.get("/frijay/events/")
        self.assertEqual(response.status_code, 200)

    '''Test the about.html page'''
    def test_aboutPage(self):
        response = self.client.get("/frijay/about/")
        self.assertEqual(response.status_code, 200)

    '''Test the login.html page'''
    def test_loginPage(self):
        response = self.client.get("/frijay/login")
        self.assertEqual(response.status_code, 200)

    '''Test the signup.html'''
    def test_signUpPage(self):
        response = self.client.get("/frijay/signup/")
        self.assertEqual(response.status_code, 200)