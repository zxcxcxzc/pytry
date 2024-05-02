from unittest.mock import patch
from bonjing import get_current_ip, get_ipv6_address

class MockLabel:
    def __init__(self):
        self.text = None
    
    def config(self, **kwargs):
        self.text = kwargs.get('text')

@patch('bonjing.tkinter.Tk')  # Mock the tk.Tk() call
def test_get_current_ip(mock_tk):
    label = MockLabel()
    get_current_ip(label)
    assert label.text.startswith("Current IPv4 address:")

@patch('bonjing.tkinter.Tk')  # Mock the tk.Tk() call
def test_get_ipv6_address(mock_tk):
    label = MockLabel()
    get_ipv6_address(label)
    assert label.text is not None
