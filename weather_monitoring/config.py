import os
from dotenv import load_dotenv

load_dotenv()

# Configuration settings
API_KEY = os.getenv("API_KEY")
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
FETCH_INTERVAL = 5  # in minutes
TEMP_UNIT = "Celsius"  # Can be "Celsius" or "Fahrenheit"
THRESHOLDS = {
    'temperature': 35  # User-defined threshold for alerting
}
