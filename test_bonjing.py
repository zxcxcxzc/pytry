import socket
from bonjing import get_current_ip, get_ipv6_address

def test_get_current_ip():
    # Mocking the socket.gethostbyname function
    # Replace this with a valid IP address for your test environment
    expected_ip = "192.168.1.100"
    socket.gethostbyname = lambda x: expected_ip
    assert get_current_ip() == expected_ip

def test_get_ipv6_address():
    # Mocking the socket.getaddrinfo function
    # Replace this with valid IPv6 addresses for your test environment
    expected_ipv6_addresses = ["fe80::1", "2001:db8::1"]
    socket.getaddrinfo = lambda x, y: [(None, None, None, None, (ipv6_address, None)) for ipv6_address in expected_ipv6_addresses]
    
    assert get_ipv6_address() == expected_ipv6_addresses[0]  # Assuming we only expect the first IPv6 address
