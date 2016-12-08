from django.test import TestCase
from bs4 import BeautifulSoup
#from urllib import urlopen
from urllib.request import urlopen

html = urlopen('https://shabbattable.herokuapp.com/').read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.title.get_text())

class TestPages(TestCase):

    def test_navbar_title(self):
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.findAll('a',{'class' : 'navbar-brand'})
        self.assertEqual(title[0].get_text(), 'Frijay')

    def test_navbar_buttons(self):
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        buttons = soup.findAll('a')
        self.assertEquals(buttons[1].get_text(), ' Join a Dinner')
        self.assertEquals(buttons[2].get_text(), 'About Us')
        self.assertEquals(buttons[3].get_text(), 'How It Works')
        self.assertEquals(buttons[4].get_text(), ' Login')
        self.assertEquals(buttons[5].get_text(), ' Sign Up')