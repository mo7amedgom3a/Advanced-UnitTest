# src/weather.py

import requests

class WeatherDataFetcher:
    """A class to fetch and store weather data."""

    def __init__(self):
        self.database = {}

    def fetch_weather(self, city):
        """Fetches weather data for a given city from an external API."""
        try:
            response = requests.get(f"https://wttr.in/{city}?format=j1")
            response.raise_for_status() # Raise an exception for 4xx/5xx status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to fetch weather data: {e}")
            return None

    def save_weather_data(self, city, data):
        """Saves the weather data for a city into the local database."""
        self.database[city] = data

    def get_weather_data(self, city):
        """Retrieves the weather data for a city from the local database."""
        return self.database[city] if city in self.database else None

