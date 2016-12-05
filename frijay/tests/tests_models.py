"""Unittests for the frijay app

Models to be tested: Event,
"""
import unittest
from unittest.mock import Mock
from frijay.models import Event


# Create your tests here.
class UnittestEventModel(unittest.TestCase):
    """Unittests for the Event Model"""

    def test_mock_string_representation(self):
        """Unit test the string representation"""
        mock_instance = Mock(spec=Event)
        mock_instance.title = "My title"
        self.assertEqual(Event.__str__(mock_instance), "My title")
