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
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    '''Test the reservation.html page'''
    def test_reservationPage(self):
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)

    '''Test the events.html page'''
    def test_eventsPage(self):
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)

    '''Test the about.html page'''
    def test_aboutPage(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    '''Test the login.html page'''
    def test_loginPage(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    '''Test the signup.html'''
    def test_signUpPage(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        user = User.objects.create(username='alberto')
        user.set_password('frijay')
        user.save()

        #self.client.login(username='alberto', password='frijay')

        response = self.client.post('/login/', username='frijay', password='frijay_pass', follow = True)

        self.assertTrue(response.context['user'].is_active)