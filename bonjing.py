#search function
#yo
import requests
import tkinter as tk
from tkinter import simpledialog, messagebox
import socket
import subprocess

def get_current_ip():
    # Get the current IPv4 address of the machine
    hostname = socket.gethostname()
    current_ip = socket.gethostbyname(hostname)
    ip_label.config(text=f"Current IPv4 address: {current_ip} (Hostname: {hostname})")

def change_ip():
    # Prompt the user to enter a new IPv4 address
    new_ip = simpledialog.askstring("Change IPv4 Address", "Enter the new IPv4 address:")
    if new_ip:
        ip_label.config(text="New IPv4 address: " + new_ip)

def get_ipv6_address():
    # Get the current IPv6 address of the machine
    hostname = socket.gethostname()
    ipv6_addresses = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(hostname, None) if addrinfo[0] == socket.AF_INET6]
    if ipv6_addresses:
        ipv6_address = ipv6_addresses[0]  # Only display the first IPv6 address if multiple exist
        ipv6_label.config(text=f"Current IPv6 address: {ipv6_address} (Hostname: {hostname})")
    else:
        ipv6_label.config(text="No IPv6 address found")

def change_ipv6_address():
    # Prompt the user to enter a new IPv6 address
    new_ipv6 = simpledialog.askstring("Change IPv6 Address", "Enter the new IPv6 address:")
    if new_ipv6:
        ipv6_label.config(text="New IPv6 address: " + new_ipv6)

def get_connected_devices():
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "network"]).decode("utf-8")
        device_info = f"Connected devices:\n{output}"
        devices_label.config(text=device_info)
    except subprocess.CalledProcessError:
        devices_label.config(text="Failed to retrieve connected devices information.")

def show_ip_page():
    # Hide the index page widgets
    index_frame.pack_forget()
    # Show the IP page widgets
    ip_frame.pack()

def show_connection_checker():
    # Hide the index page widgets
    index_frame.pack_forget()
    # Show the connection checker widgets
    connection_frame.pack()
    # Get connected devices information
    get_connected_devices()

def show_search_ip_page():
    # Hide the index page widgets
    index_frame.pack_forget()
    # Show the search IP page widgets
    search_ip_frame.pack()

# Create the main window
root = tk.Tk()
root.title("IP Address Management")

# Font settings for the header
header_font = ("Helvetica", 16)

# Create the index page
index_frame = tk.Frame(root)

# Welcome message
index_label = tk.Label(index_frame, text="Welcome to The IP Quick Checker", font=header_font, pady=20)
index_label.pack()

# Button to navigate to the IP page (renamed to "Manage IP")
ip_button = tk.Button(index_frame, text="Manage IP", command=show_ip_page)
ip_button.pack()

# Button to navigate to the connection checker
connection_button = tk.Button(index_frame, text="Connection Checker", command=show_connection_checker)
connection_button.pack()

# Button to navigate to the search IP page
search_ip_button = tk.Button(index_frame, text="Search IP", command=show_search_ip_page)
search_ip_button.pack()

# Pack the index frame
index_frame.pack()

# Create the IP page
ip_frame = tk.Frame(root)

# Header for the IP page
ip_header_label = tk.Label(ip_frame, text="Manage IP", font=header_font)
ip_header_label.pack()

# Button to go back to the index page
ip_back_button = tk.Button(ip_frame, text="Back", command=lambda: (ip_frame.pack_forget(), index_frame.pack()), anchor='nw')
ip_back_button.pack()

# Create a label to display IPv4 addresses
ip_label = tk.Label(ip_frame, text="")
ip_label.pack()

# Create buttons to show current IPv4 and change IPv4
get_ip_button = tk.Button(ip_frame, text="Show Current IPv4", command=get_current_ip)
get_ip_button.pack()

change_ip_button = tk.Button(ip_frame, text="Change IPv4 Address", command=change_ip)
change_ip_button.pack()

# Create a label to display IPv6 addresses
ipv6_label = tk.Label(ip_frame, text="")
ipv6_label.pack()

# Create buttons to show current IPv6 and change IPv6
get_ipv6_button = tk.Button(ip_frame, text="Show Current IPv6", command=get_ipv6_address)
get_ipv6_button.pack()

change_ipv6_button = tk.Button(ip_frame, text="Change IPv6 Address", command=change_ipv6_address)
change_ipv6_button.pack()

# Pack the IP frame (initially hidden)
ip_frame.pack_forget()

# Create the connection checker page
connection_frame = tk.Frame(root)

# Header for the connection checker page
connection_header_label = tk.Label(connection_frame, text="Connection Checker", font=header_font)
connection_header_label.pack()

# Button to go back to the index page
connection_back_button = tk.Button(connection_frame, text="Back", command=lambda: (connection_frame.pack_forget(), index_frame.pack()), anchor='nw')
connection_back_button.pack()

# Create a label to display connected devices
devices_label = tk.Label(connection_frame, text="")
devices_label.pack()

# Create a button to show connected devices
get_devices_button = tk.Button(connection_frame, text="Show Connected Devices", command=get_connected_devices)
get_devices_button.pack()

# Pack the connection checker frame (initially hidden)
connection_frame.pack_forget()

# Create the search IP page
search_ip_frame = tk.Frame(root)

# Header for the search IP page
search_ip_header_label = tk.Label(search_ip_frame, text="Search IP", font=header_font)
search_ip_header_label.pack()

# Button to go back to the index page
search_ip_back_button = tk.Button(search_ip_frame, text="Back", command=lambda: (search_ip_frame.pack_forget(), index_frame.pack()), anchor='nw')
search_ip_back_button.pack()

# Entry field for inputting the IP address
ip_entry = tk.Entry(search_ip_frame)
ip_entry.pack()

# Label for displaying IPv4 address
ip_v4_label = tk.Label(search_ip_frame, text="")
ip_v4_label.pack()

# Text widget for displaying details
details_text = tk.Text(search_ip_frame, height=10, width=50)
details_text.pack()

def get_ip_info(ipv4_address):
    try:
        # Retrieve detailed IP information from ipinfo.io
        details_response = requests.get(f"https://ipinfo.io/{ipv4_address}/json")
        if details_response.status_code == 200:
            details_data = details_response.json()
            update_details(details_data)
        else:
            update_details({"error": "Error fetching details"})
    except requests.exceptions.RequestException as e:
        update_details({"error": f"Error: {e}"})

def get_ip_info_wrapper():
    ipv4_address = ip_entry.get()
    ip_v4_label.config(text=f"IPv4: {ipv4_address}")
    get_ip_info(ipv4_address)

def update_details(details_data):
    details_text.delete('1.0', tk.END)
    if "error" in details_data:
        details_text.insert(tk.END, details_data["error"])
    else:
        for key, value in details_data.items():
            details_text.insert(tk.END, f"{key}: {value}\n")

# Button to search for IP details
search_ip_button = tk.Button(search_ip_frame, text="Search", command=get_ip_info_wrapper)
search_ip_button.pack()

# Pack the search IP frame (initially hidden)
search_ip_frame.pack_forget()

# Run the Tkinter event loop
root.mainloop()
