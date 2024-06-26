import pytest
from unittest.mock import patch
from tkinter import messagebox

# Import pyvirtualdisplay for virtual display functionality
from pyvirtualdisplay import Display

# Import the functions to be tested
from bonjing import get_current_ip, get_ipv6_address, login, check_connection

# Mock the necessary modules and functions
@pytest.fixture
def mock_ui():
    with patch('bonjing.login_window'), \
         patch('bonjing.root'), \
         patch('bonjing.username_entry'), \
         patch('bonjing.password_entry'):
        
        # Create a virtual display
        display = Display(visible=0, size=(800, 600))
        display.start()

        yield

        # Stop the virtual display after all tests are done
        display.stop()

@pytest.fixture
def mock_psutil_net_if_addrs():
    return {
        'Ethernet': [
            type('addr', (), {'address': '192.168.1.2', 'family': 'AF_INET'}),
            type('addr', (), {'address': 'fe80::1', 'family': 'AF_INET6'})
        ]
    }

@pytest.fixture
def mock_geocoder_ip():
    return type('Geocoder', (), {'lat': 37.7749, 'lng': -122.4194, 'city': 'San Francisco', 'region': 'California', 'ok': True})

@pytest.fixture
def mock_requests_get():
    return type('Response', (), {'status_code': 200})

# Test cases
def test_get_current_ip(mock_ui, mock_psutil_net_if_addrs):
    with patch('psutil.net_if_addrs', return_value=mock_psutil_net_if_addrs):
        ip_address = get_current_ip('Ethernet')
        assert ip_address == '192.168.1.2'

def test_get_ipv6_address(mock_ui, mock_psutil_net_if_addrs):
    with patch('psutil.net_if_addrs', return_value=mock_psutil_net_if_addrs):
        ipv6_address = get_ipv6_address()
        assert ipv6_address == 'fe80::1'

def test_login_successful(mock_ui):
    with patch('bonjing.messagebox.showerror') as mock_showerror:
        login()
        mock_showerror.assert_not_called()

def test_login_failed(mock_ui):
    with patch('bonjing.messagebox.showerror') as mock_showerror:
        username_entry = 'invalid'
        password_entry = 'invalid'
        login()
        mock_showerror.assert_called_once_with("Login failed", "Invalid username or password")

def test_check_connection(mock_ui, mock_requests_get):
    with patch('requests.get', return_value=mock_requests_get):
        check_connection()
        messagebox.showinfo.assert_called_once_with("Connection Status", "Connected to the internet!")
