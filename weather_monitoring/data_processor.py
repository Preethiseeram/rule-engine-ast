from src.utilities import kelvin_to_celsius

class WeatherDataProcessor:
    def process_weather_data(self, weather_data):
        temp_in_kelvin = weather_data['main']['temp']
        temp_in_celsius = kelvin_to_celsius(temp_in_kelvin)
        # Add more processing logic for rollups and aggregates
        return {
            "city": weather_data['name'],
            "temperature": temp_in_celsius,
            "condition": weather_data['weather'][0]['main']
        }
