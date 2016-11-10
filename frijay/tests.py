from django.test import TestCase
from .models import Event

# Create your tests here.
class EventModelTest(TestCase):

    def test_string_representation(self):
        event = Event(title="My event title")
        self.assertEqual(str(event), event.title)
