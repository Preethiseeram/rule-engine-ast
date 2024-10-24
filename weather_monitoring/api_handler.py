import requests
from config.config import API_KEY

class WeatherAPIHandler:
    def __init__(self, cities):
        self.api_key = API_KEY
        self.cities = cities

    def get_weather_data(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data for {city}")
            return None
