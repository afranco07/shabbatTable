
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from frijay.models import Event
from bs4 import BeautifulSoup

class ViewsTest(TestCase):
    """Tests all functions in views.py"""

    def setUp(self):
        """Creates the User, and tests if they can login"""
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


    def test_user_login_view(self):
        """Tests the function user_login(request) in views.py"""
        response = self.client.post('/login',
                                    {'username': 'bob',
                                     'password': 'temp'}, )
        self.assertTrue(response.status_code, 200)


    def test_logout_functionality(self):
        """Tests if user can logout and gets redirected"""
        self.client.login(username='bob', password='temp')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)



    def test_landing_page(self):
        """Tests the landing page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        searchresponse = self.client.post('/', {'search': 'queens'})
        self.assertEqual(searchresponse.status_code, 200)


    def test_reservation_page(self):
        """Tests the reservations page """
        self.client.login(username='bob', password='temp')
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)


    def test_events_page(self):
        """Tests the events page"""
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)


    def test_about_page(self):
        """Tests the about page"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


    def test_login_page(self):
        """Tests the login page"""
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)


    def test_signup_page(self):
        """Tests the signup page"""
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        data = {'first_name' : "bob",
                'last_name' : "franklin",
                'username' : "bobf",
                'email' : "bob@mail.com",
                'password' : "temp"}
        formResponse = self.client.post('/signup/', data)
        self.assertEqual(formResponse.status_code, 200)
        # form = UserForm(data)
        #self.assertTrue(form.is_valid())

    def test_host_dinner(self):
        """Tests the host.html page"""
        self.client.login(username='bob', password='temp')
        response = self.client.get("/host/")
        self.assertEqual(response.status_code, 200)

    def test_reservations(self):
        """Test the myevents.html"""
        self.client.login(username='bob', password='temp')
        response = self.client.get("/myevents/")
        self.assertEqual(response.status_code, 200)

    def test_how_it_works(self):
        """Tests the howitworks page"""
        response = self.client.get("/howitworks/")
        self.assertEqual(response.status_code, 200)


    def test_reservations_events(self):
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
        response = self.client.get("/events/"+ str(event_id) + "/")
        self.assertContains(response, "Friday Dinner with the mr. president")
        self.assertEqual(response.status_code, 200)


    def test_one_event(self):
        """Test whether our events show up on the homepage.

        Adding one event and testing whether it will show up
        on the featured events on index page"""
        Event.objects.create(
            title='Shabbat',
            address='testaddress',
            city='Brooklyn',
            state='New York',
            phone='1231231234',
            date='2016-12-07',
            time1='03:24:12',
            time2="03:24:12",
            openSeats='10',
            additionalDetails='None', )
        response = self.client.get('/')
        html = response.content
        html = BeautifulSoup(html, "html.parser")
        self.assertEquals(html.title.string, 'Frijay')
        for x in response.context:
            self.assertEquals(x['Events'][0].title, 'Shabbat')
            self.assertEquals(x['Events'][0].address, 'testaddress')
            self.assertEquals(x['Events'][0].city, 'Brooklyn')
            self.assertEquals(x['Events'][0].state, 'New York')
            self.assertEquals(x['Events'][0].phone, 1231231234)
        event_box = html.body.find(attrs={"class": "hovereffect"})
        self.assertEquals(event_box.h3.string, 'Shabbat')
        self.assertEquals(event_box.h4.string, 'Brooklyn')
        self.assertEqual(event_box.select_one("p:nth-of-type(3)").text, 'Date: Dec. 7, 2016')
        self.assertEquals(event_box.h5.text, 'Open Seats: 10')


    def test_two_events(self):
        """Adding two events and testing whether they will show up on the
        featured events on index page"""
        Event.objects.create(
            title='Frijay',
            address='testaddress2',
            city='Queens',
            state='New York',
            phone='1233213221',
            date='2016-12-09',
            time1='03:24:12',
            time2="03:24:12",
            openSeats='2',
            additionalDetails='None', )
        Event.objects.create(
            title='Shabbat',
            address='testaddress',
            city='Brooklyn',
            state='New York',
            phone='1231231234',
            date='2016-12-07',
            time1='03:24:12',
            time2="03:24:12",
            openSeats='10',
            additionalDetails='None', )
        response = self.client.get('/')
        html = response.content
        html = BeautifulSoup(html, "html.parser")
        self.assertEquals(html.title.string, 'Frijay')
        for x in response.context:
            self.assertEquals(x['Events'][0].title, 'Frijay')
            self.assertEquals(x['Events'][0].address, 'testaddress2')
            self.assertEquals(x['Events'][0].city, 'Queens')
            self.assertEquals(x['Events'][0].state, 'New York')
            self.assertEquals(x['Events'][0].phone, 1233213221)

            self.assertEquals(x['Events'][1].title, 'Shabbat')
            self.assertEquals(x['Events'][1].address, 'testaddress')
            self.assertEquals(x['Events'][1].city, 'Brooklyn')
            self.assertEquals(x['Events'][1].state, 'New York')
            self.assertEquals(x['Events'][1].phone, 1231231234)

        event_box = html.body.find_all(attrs={"class": "hovereffect"})
        self.assertEquals(event_box[0].h3.string, 'Frijay')
        self.assertEquals(event_box[0].h4.string, 'Queens')
        self.assertEqual(event_box[0].select_one("p:nth-of-type(3)").text, 'Date: Dec. 9, 2016')
        self.assertEquals(event_box[0].h5.text, 'Open Seats: 2')
        self.assertEquals(event_box[1].h3.string, 'Shabbat')
        self.assertEquals(event_box[1].h4.string, 'Brooklyn')
        self.assertEqual(event_box[1].select_one("p:nth-of-type(3)").text, 'Date: Dec. 7, 2016')
        self.assertEquals(event_box[1].h5.text, 'Open Seats: 10')

    def test_no_events(self):
        """Testing will the output print statment will show up
        upon no events in the database"""
        response = self.client.get('/')
        error_msg = 'Sorry, no events right now :( Please come back later.'
        self.assertContains(response, error_msg)


    def test_one_event_eventpage(self):
        """Adding one event and testing whether it will show up on the events page"""
        Event.objects.create(
            title='Shabbat',
            address='testaddress',
            city='Brooklyn',
            state='New York',
            phone='1231231234',
            date='2016-12-07',
            time1='03:24:12',
            time2="03:24:12",
            openSeats='10',
            additionalDetails='None', )
        response = self.client.get('/events/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    def test_no_events_eventspage(self):
        """Testing the events page on no events in Database"""
        response = self.client.get('/events/')
        self.assertContains(response, 'Sorry, no events right now :('
                                      ' Please come back later.')

    def test_login(self):
        """Test for login"""
        username = 'ayaz'
        password = 'test'
        user = get_user_model()
        user.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
