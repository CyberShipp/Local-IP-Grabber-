import customtkinter as ctk
import socket
import requests
import platform

def get_geolocation(ip_address):
    # Request geolocation data from ipstack API
    access_key = 'YOUR_IPSTACK_ACCESS_KEY'  # Replace with your ipstack access key
    url = f'http://api.ipstack.com/{ip_address}?access_key={access_key}'
    response = requests.get(url)
    data = response.json()

    # Extract city and state information
    city = data['city']
    region = data['region_name']

    return city, region

def button_callback():
    # Retrieve public IP address
    response = requests.get('https://api.ipify.org?format=json')
    public_ip_address = response.json()['ip']

    # Retrieve private IP address
    private_ip_address = socket.gethostbyname(socket.getfqdn())

    # Get operating system and hostname
    operating_system = platform.system()
    hostname = socket.gethostname()

    # Display the IP addresses, operating system, and hostname in the same window
    ip_label.configure(text=f"Public IP Address: {public_ip_address}\n"
                            f"Private IP Address: {private_ip_address}\n"
                            f"Operating System: {operating_system}\n"
                            f"Hostname: {hostname}")

    # Get geolocation information for public IP address
    city, region = get_geolocation(public_ip_address)
    
    # Display city and state information
    geolocation_label.configure(text=f"City: {city}\n"
                                     f"State: {region}")

app = ctk.CTk()
app.title("GetIP")
app.geometry("400x350")

created_by_label = ctk.CTkLabel(app, text="Created by Ethan Shipp", font=("Arial", 10))
created_by_label.grid(row=0, column=0, padx=20, pady=10)

button = ctk.CTkButton(app, text="What's my IP?", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)

ip_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
ip_label.grid(row=2, column=0, padx=20, pady=10)

geolocation_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
geolocation_label.grid(row=3, column=0, padx=20, pady=10)

app.grid_columnconfigure(0, weight=1)
app.mainloop()