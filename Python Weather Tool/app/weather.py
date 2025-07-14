import requests
from config import CITY, API_KEY

# Function to fetch the weather from the API
def fetch_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Weather data not available"
    
    data = response.json()

    return format_weather(data)

# Function to format the weather data for display

def format_weather(data):
    desc = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    wind_dir = data['wind'].get('deg', 'N/A')
    city = data['name']
    country = data['sys']['country']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    sunrise_time = format_time(sunrise)
    sunset_time = format_time(sunset)
    return (f"Weather in {city}, {country}:\n"
            f"Description: {desc}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Wind Direction: {wind_dir}°\n"
            f"Sunrise: {sunrise_time}\n"
            f"Sunset: {sunset_time}")

