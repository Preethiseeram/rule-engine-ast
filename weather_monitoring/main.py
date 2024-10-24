import time
from src.api_handler import WeatherAPIHandler
from src.data_processor import WeatherDataProcessor
from src.alert_system import WeatherAlertSystem
from src.visualization import WeatherVisualization
from config.config import CITIES, FETCH_INTERVAL, THRESHOLDS

weather_api = WeatherAPIHandler(CITIES)
data_processor = WeatherDataProcessor()
alert_system = WeatherAlertSystem(THRESHOLDS)
visualization = WeatherVisualization()

while True:
    for city in CITIES:
        weather_data = weather_api.get_weather_data(city)
        if weather_data:
            processed_data = data_processor.process_weather_data(weather_data)
            alert_system.check_alert(processed_data)
            # Optionally store data and call visualization methods
    time.sleep(FETCH_INTERVAL * 60)
