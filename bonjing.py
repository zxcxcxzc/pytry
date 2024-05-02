import tkinter as tk
import socket

def get_current_ip():
    # Get the current IPv4 address of the machine
    return socket.gethostbyname(socket.gethostname())
    pass

def get_ipv6_address():
    # Get the current IPv6 address of the machine
    ipv6_addresses = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(socket.gethostname(), None) if addrinfo[0] == socket.AF_INET6]
    return ipv6_addresses[0] if ipv6_addresses else None
    pass

def update_ip_labels():
    # Update the labels with the current IP addresses
    current_ip = get_current_ip()
    ip_label.config(text="Current IPv4 address: " + current_ip)

    ipv6_address = get_ipv6_address()
    if ipv6_address:
        ipv6_label.config(text="Current IPv6 address: " + ipv6_address)
    else:
        ipv6_label.config(text="No IPv6 address found")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("IP Address Viewer")

    # Create a label to display IPv4 addresses
    ip_label = tk.Label(root, text="")
    ip_label.pack(pady=10)

    # Create buttons to show current IPv4
    get_ip_button = tk.Button(root, text="Show Current IPv4", command=update_ip_labels)
    get_ip_button.pack()

    # Create a label to display IPv6 addresses
    ipv6_label = tk.Label(root, text="")
    ipv6_label.pack(pady=10)

    # Create buttons to show current IPv6
    get_ipv6_button = tk.Button(root, text="Show Current IPv6", command=update_ip_labels)
    get_ipv6_button.pack()

    # Run the Tkinter event loop
    root.mainloop()
