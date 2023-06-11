# Local-IP-Grabber-
It imports:

customtkinter for creating the GUI.
socket for retrieving IP address and hostname information.
requests for making HTTP requests to external APIs.
platform for retrieving information about the operating system.
The get_geolocation() function is defined, which takes an IP address as input and uses the ipstack API to request geolocation data. It extracts the city and region information and returns them.

The button_callback() function is defined, which serves as the event handler for the "What's my IP?" button. When the button is clicked, it performs the following actions:

Retrieves the public IP address using the ipify API.
Retrieves the private IP address using the socket module.
Retrieves the operating system using the platform module.
Retrieves the hostname using the socket module.
Updates the ip_label and geolocation_label widgets with the retrieved information.
The app object is created using ctk.CTk(), which represents the main application window. The title of the window is set to "GetIP" and the dimensions are set to 400x300 pixels.

A button labeled "What's my IP?" is created using ctk.CTkButton(), and its command is set to button_callback() so that the function is executed when the button is clicked. The button is placed in the grid layout at row 0, column 0, with some padding.

Two labels (ip_label and geolocation_label) are created using ctk.CTkLabel(). These labels will display the IP address, geolocation, operating system, and hostname information. They are initially empty and will be updated dynamically when the button is clicked. They are placed in the grid layout at rows 1 and 2, with some padding.

The app.grid_columnconfigure(0, weight=1) line configures the first column of the grid to expand and fill the available space horizontally.

Finally, the GUI application is started with app.mainloop(), which enters the event loop and keeps the application running until the user closes the window.

When the user clicks the "What's my IP?" button, the script retrieves the public and private IP addresses, the geolocation information, and the operating system and hostname. These details are then displayed in the respective labels in the GUI window.
