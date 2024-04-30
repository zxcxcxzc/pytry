# test_ip_management.py

import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import simpledialog
import ip_management

class MockLabel:
    def __init__(self):
        self.text = None
    
    def config(self, **kwargs):
        self.text = kwargs.get('text')

class TestIPManagement(unittest.TestCase):

    @patch('ip_management.socket.gethostname', return_value='test_hostname')
    @patch('ip_management.socket.gethostbyname', return_value='192.168.1.100')
    def test_get_current_ip(self, mock_gethostbyname, mock_gethostname):
        ip_label = MockLabel()
        ip_management.get_current_ip(ip_label)
        self.assertEqual(ip_label.text, 'Current IPv4 address: 192.168.1.100 (Hostname: test_hostname)')

    @patch('tkinter.simpledialog.askstring', return_value='192.168.1.200')
    def test_change_ip(self, mock_askstring):
        ip_label = MockLabel()
        ip_management.change_ip()
        self.assertEqual(ip_label.text, 'New IPv4 address: 192.168.1.200')

    @patch('ip_management.socket.gethostname', return_value='test_hostname')
    @patch('ip_management.socket.getaddrinfo', return_value=[(None, None, None, None, ('fe80::1', None))])
    def test_get_ipv6_address(self, mock_getaddrinfo, mock_gethostname):
        ipv6_label = MockLabel()
        ip_management.get_ipv6_address(ipv6_label)
        self.assertEqual(ipv6_label.text, 'Current IPv6 address: fe80::1 (Hostname: test_hostname)')

    @patch('tkinter.simpledialog.askstring', return_value='fe80::2')
    def test_change_ipv6_address(self, mock_askstring):
        ipv6_label = MockLabel()
        ip_management.change_ipv6_address()
        self.assertEqual(ipv6_label.text, 'New IPv6 address: fe80::2')

    @patch('subprocess.check_output', return_value='Connected devices:\nDevice 1\nDevice 2')
    def test_get_connected_devices(self, mock_check_output):
        devices_label = MockLabel()
        ip_management.get_connected_devices(devices_label)
        self.assertEqual(devices_label.text, 'Connected devices:\nDevice 1\nDevice 2')

    def test_show_ip_page(self):
        index_frame = tk.Frame(ip_management.root)
        ip_frame = tk.Frame(ip_management.root)
        index_frame.pack()
        ip_management.show_ip_page()
        self.assertFalse(index_frame.winfo_ismapped())
        self.assertTrue(ip_frame.winfo_ismapped())

    def test_show_connection_checker(self):
        index_frame = tk.Frame(ip_management.root)
        connection_frame = tk.Frame(ip_management.root)
        index_frame.pack()
        ip_management.show_connection_checker()
        self.assertFalse(index_frame.winfo_ismapped())
        self.assertTrue(connection_frame.winfo_ismapped())

    def test_show_search_ip_page(self):
        index_frame = tk.Frame(ip_management.root)
        search_ip_frame = tk.Frame(ip_management.root)
        index_frame.pack()
        ip_management.show_search_ip_page()
        self.assertFalse(index_frame.winfo_ismapped())
        self.assertTrue(search_ip_frame.winfo_ismapped())

if __name__ == '__main__':
    unittest.main()
