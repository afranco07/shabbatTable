from django.test import TestCase
from django.contrib.auth import get_user_model
from frijay.models import Event
from django.contrib.auth.models import User
from django.test import Client
from frijay.forms import UserForm

class ViewsTest(TestCase):

    '''Creates the User, and tests if they can login'''
    def setUp(self):
        self.client = Client()
        self.guest1 = User.objects.create_user(
            username='bob',
            password='temp',
            email='',
            first_name='Robert',
            last_name='Knapp', )
        self.host = User.objects.create_user(
            username="abrahamlincoln",
            password="password",
            email="lincoln@email.com",
            first_name='Abraham',
            last_name='Lincoln', )


    def test_login_functionality(self):
        """Tests if a user is active and can login"""
        self.client.login(username='bob', password='temp')
        self.assertTrue(self.guest1)
        self.assertTrue(self.guest1.is_active)
        self.assertTrue(self.guest1.is_authenticated)
        # pass


    def test_user_login_view(self):
        """Tests the function user_login(request) in views.py"""
        response = self.client.post('/login', {'username': 'bob', 'password':
            'temp'})
        self.assertTrue(response.status_code, 200)


    def test_logout_fucntionality(self):
        self.client.login(username='bob', password='temp')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)


    '''Test the index.html page'''
    def test_indexPage(self):
        """Tests the landing page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        searchResponse = self.client.post('/', {'search' : 'queens'})
        self.assertEqual(searchResponse.status_code, 200)


    def test_reservationPage(self):
        """Tests the reservations page """
        self.client.login(username='bob', password='temp')
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)


    '''Test the events.html page'''
    def test_eventsPage(self):
        """Tests the events page"""
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)


    '''Test the about.html page'''
    def test_aboutPage(self):
        """Tests the about page"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


    '''Test the login.html page'''
    def test_loginPage(self):
        """Tests the login page"""
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)


    def test_signUpPage(self):
        """Tests the signup page"""
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        data ={'first_name' : "bob",
               'last_name' : "franklin",
               'username' : "bobf",
               'email' : "bob@mail.com",
               'password' : "temp"}
        formResponse = self.client.post('/signup/', data)
        self.assertEqual(formResponse.status_code, 200)
        form = UserForm(data)
        #self.assertTrue(form.is_valid())


    def test_hostDinner(self):
        """Tests the host.html page"""
        self.client.login(username='bob', password='temp')
        response = self.client.get("/host/")
        self.assertEqual(response.status_code, 200)


    def test_reservations(self):
        """Test the myevents.html"""
        self.client.login(username='bob', password='temp')
        response = self.client.get("/myevents/")
        self.assertEqual(response.status_code, 200)


    def test_reservationsEvents(self):
        """Tests whether a specific event shows up in its own page"""
        self.client.login(username='abrahamlincoln', password='password')
        event = Event.objects.create(
            title="Friday Dinner with the mr. president",
            host=self.host,
            address="160 Covent Ave",
            city="New York",
            state="NY",
            phone="2126507000",
            date="2017-01-02",
            time1="05:23:00",
            time2="07:23:00",
            openSeats="4",
            additionalDetails="Guests, please bring a bottle of wine.")
        event_id = event.id
        # TODO complete this test
        response = self.client.get("/events/"+ str(event_id) + "/")
        # print(dir(response))
        # print(response._container)
        self.assertContains(response, "Friday Dinner with the mr. president")
        self.assertEqual(response.status_code, 200)


    def test_one_event(self):
        """Test whether our events show up on the homepage
        Adding one event and testing whether it will show up on the featured events on index page"""
        Event.objects.create(title='Shabbat',address='testaddress',city='Brooklyn',state='New York',
                             phone='1231231234',date='2016-12-07',time1='03:24:12',time2="03:24:12",
                             openSeats='10',additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    def test_two_events(self):
        """Adding two events and testing whether they will show up on the
        featured events on index page"""
        Event.objects.create(title='Frijay', address='testaddress2', city='Queens', state='New York',
                             phone='1233213221', date='2016-12-07', time1='03:24:12', time2="03:24:12",
                             openSeats='2', additionalDetails='None')
        Event.objects.create(title='Shabbat', address='testaddress', city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07', time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Frijay')
        self.assertContains(response, 'Queens')
        self.assertContains(response, '2')

    def test_no_events(self):
        """Testing will the output print statment will show up upon no events in the database"""
        response = self.client.get('/')
        self.assertContains(response, 'Sorry, no events right now :( Please come back later.')

    def test_one_event_eventpage(self):
        """Test whether events show up on Events page
        Adding one event and testing whether it will show up on the events page"""
        Event.objects.create(title='Shabbat', address='testaddress', city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07', time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/events/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    '''Testing the events page on no events in Database'''
    def test_no_events_eventspage(self):
        response = self.client.get('/events/')
        self.assertContains(response, 'Sorry, no events right now :( Please come back later.')


