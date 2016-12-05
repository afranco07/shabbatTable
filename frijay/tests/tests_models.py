"""Unittests for the models in frijay app

Models to be tested: Event, Reservation
"""
import unittest
from unittest.mock import Mock


# Create your tests here.
class UnittestEventModel(unittest.TestCase):
    """Unittests for the Event Model"""
    def test_mock_string_representation(self):
        """Unit test the string representation

        Mocks an Event model and checks if __str__() returns the title
        """
        from frijay.models import Event

        mock_instance = Mock(spec=Event)
        mock_instance.title = "My title"
        self.assertEqual(Event.__str__(mock_instance), "My title")


class UnittestReservationModel(unittest.TestCase):
    """Unittests for the Reservation Model"""
    def test_mock_string_representation(self):
        """Unit test the string representation

        Mocks a Reservation model and checks if __str__() returns the
        Reservation's event title
        """
        from frijay.models import Reservation

        mock_instance = Mock(spec=Reservation)
        mock_instance.event.name = "My Event title"
        self.assertEqual(Reservation.__str__(mock_instance),
                         "My Event title")
