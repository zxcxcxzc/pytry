# test_bonjing.py

import unittest
from unittest.mock import patch, MagicMock
from bonjing import get_current_ip, get_ipv6_address

class MockLabel:
    def __init__(self):
        self.text = None
    
    def config(self, **kwargs):
        self.text = kwargs.get('text')

class TestGetIPAddress(unittest.TestCase):

    @patch('bonjing.tkinter.Tk', MagicMock)  # Mocking Tkinter to avoid creating a graphical window
    def test_get_current_ip(self):
        label = MockLabel()
        get_current_ip(label)
        self.assertTrue(label.text.startswith("Current IPv4 address:"))

    @patch('bonjing.tkinter.Tk', MagicMock)  # Mocking Tkinter to avoid creating a graphical window
    def test_get_ipv6_address(self):
        label = MockLabel()
        get_ipv6_address(label)
        self.assertIsNotNone(label.text)

if __name__ == '__main__':
    unittest.main()
