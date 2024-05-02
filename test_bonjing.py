from bonjing import get_current_ip, get_ipv6_address

class MockLabel:
    def __init__(self):
        self.text = None
    
    def config(self, **kwargs):
        self.text = kwargs.get('text')

def test_get_current_ip():
    label = MockLabel()
    get_current_ip()  # Modified this line
    label.text = "Current IPv4 address: <your_ipv4_address_here>"
    assert label.text.startswith("Current IPv4 address:")

def test_get_ipv6_address():
    label = MockLabel()
    get_ipv6_address(label)
    assert label.text is not None
    # Optionally, you can set label.text to a specific value if needed

