import tkinter as tk
from PIL import ImageTk, Image
import datetime
import requests

# Function to get weather information from OpenWeatherMap API
def get_weather(city):
    api_key = "a5d4f05928abcf2152c984728077b360"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "description": data["weather"][0]["description"].capitalize(),
            "temperature": f"{data['main']['temp']}°C",
            "humidity": f"{data['main']['humidity']}%",
            "wind speed": f"{data['wind']['speed']} m/s",
            "pressure": f"{data['main']['pressure']} hPa"
        }
        return weather_data
    else:
        return None

# Function to display weather information in the window
def display_weather():
    city = city_entry.get()
    weather = get_weather(city)

    if weather:
        # Update the labels with weather information
        temperature_label.config(text=f"Temperature: {weather['temperature']}")
        humidity_label.config(text=f"Humidity: {weather['humidity']}")
        wind_speed_label.config(text=f"Wind Speed: {weather['wind speed']}")
        pressure_label.config(text=f"Pressure: {weather['pressure']}")
        description_label.config(text=f"Description: {weather['description']}")
    else:
        # Display error if weather data is not available
        temperature_label.config(text="Temperature: N/A")
        humidity_label.config(text="Humidity: N/A")
        wind_speed_label.config(text="Wind Speed: N/A")
        pressure_label.config(text="Pressure: N/A")
        description_label.config(text="Description: N/A")

# Create main window
root = tk.Tk()
root.title("Weather App")

# Set background image
bg_image = ImageTk.PhotoImage(Image.open("C:/Users/Divya/Desktop/New folder/istockphoto.jpg"))
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window

# Add heading
heading_label = tk.Label(root, text="Weather Report", font=("Helvetica", 20),fg='red')
heading_label.pack()

# Add city entry
city_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
city_entry.pack(pady=10)

# Add date and time
def update_datetime():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%d %B %Y")
    formatted_time = now.strftime("%H:%M:%S")
    date_time_label.config(text=f"Date: {formatted_date}  Time: {formatted_time}")
    date_time_label.after(1000, update_datetime)  # Update every second

date_time_label = tk.Label(root, font=("Helvetica", 12),fg='green')
date_time_label.pack()
update_datetime()

# Add search button
search_button = tk.Button(root, text="Check Weather", font=("Helvetica", 12), command=display_weather, bg="orange", fg="white")
search_button.pack()

# Load weather icons
temperature_icon = ImageTk.PhotoImage(Image.open("C:/Users/Divya/Desktop/images/Temperature_icon.png").resize((90, 90)))
humidity_icon = ImageTk.PhotoImage(Image.open("C:/Users/Divya/Desktop/images/humidity_icon.png").resize((90, 90)))
wind_speed_icon = ImageTk.PhotoImage(Image.open("C:/Users/Divya/Desktop/images/wind.png").resize((90, 90)))
pressure_icon = ImageTk.PhotoImage(Image.open("C:/Users/Divya/Desktop/images/pressure.png").resize((90, 90)))
description_icon = ImageTk.PhotoImage(Image.open("C:/Users/Divya/Desktop/images/clear.png").resize((90, 90)))

# Frame to contain weather information labels
weather_frame = tk.Frame(root,bg=root['bg'])  # Use a transparent background
weather_frame.pack(pady=10)

# Labels to display weather information
temperature_label = tk.Label(weather_frame, font=("Helvetica", 12),bg='white')
temperature_label.grid(row=0, column=0, padx=5, pady=5)
temperature_label.config(image=temperature_icon, compound=tk.TOP)

humidity_label = tk.Label(weather_frame, font=("Helvetica", 12),bg='white')
humidity_label.grid(row=0, column=1, padx=5, pady=5)
humidity_label.config(image=humidity_icon, compound=tk.TOP)

wind_speed_label = tk.Label(weather_frame, font=("Helvetica", 12),bg='white')
wind_speed_label.grid(row=0, column=2, padx=5, pady=5)
wind_speed_label.config(image=wind_speed_icon, compound=tk.TOP)

pressure_label = tk.Label(weather_frame, font=("Helvetica", 12),bg='white')
pressure_label.grid(row=1, column=0, padx=5, pady=5)
pressure_label.config(image=pressure_icon, compound=tk.TOP)

description_label = tk.Label(weather_frame, font=("Helvetica", 12),bg='white')
description_label.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
description_label.config(image=description_icon, compound=tk.TOP)

root.mainloop()







