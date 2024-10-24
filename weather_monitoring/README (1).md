
# Real-Time Weather Monitoring System

## Overview

This project is a real-time weather monitoring system that fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/) for multiple cities in India. It processes the data to generate daily weather summaries, track user-defined thresholds (like high temperatures), and trigger alerts if necessary. The project also provides visualizations for weather trends and alerts.

### Features:
- Real-time weather data retrieval at configurable intervals.
- Weather data rollups and aggregates, including:
  - Average, maximum, and minimum temperature.
  - Dominant weather condition.
- Customizable alerting thresholds (e.g., temperature > 35°C).
- Visualizations of daily summaries and historical trends.
- Extendable to additional weather parameters like humidity and wind speed.

## Project Structure

```bash
weather-monitoring/
│
├── config/
│   └── config.py            # Configuration settings (API key, cities, thresholds)
├── data/
│   └── storage.db           # Persistent storage for daily summaries (SQLite or other DB)
├── src/
│   ├── __init__.py          # Initializes the module
│   ├── api_handler.py       # Handles API communication with OpenWeatherMap
│   ├── data_processor.py    # Processes weather data (rollups, aggregates)
│   ├── alert_system.py      # Tracks thresholds and triggers alerts
│   ├── visualization.py     # Visualizes data (graphs, trends)
│   ├── utilities.py         # Utility functions (e.g., temperature conversion)
│   └── main.py              # Main script to run the system
├── tests/
│   ├── test_api_handler.py   # Tests for API handler
│   ├── test_data_processor.py# Tests for weather data processing
│   ├── test_alert_system.py  # Tests for alerting system
│   ├── test_utilities.py     # Tests for utility functions
├── .env                     # Environment variables (API key, etc.)
├── requirements.txt          # List of dependencies (e.g., requests, matplotlib)
└── README.md                 # Project documentation
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-monitoring.git
cd weather-monitoring
```

### 2. Set up a Python Virtual Environment
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
You need an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

1. Create a `.env` file in the project root directory:
   ```bash
   touch .env
   ```
2. Add your OpenWeatherMap API key to the `.env` file:
   ```
   API_KEY=your_openweather_api_key
   ```

### 5. Running the Application

To start fetching real-time weather data and processing it:
```bash
python src/main.py
```

### 6. Configuration

All configuration settings can be found in `config/config.py`. Here, you can:
- Adjust the `FETCH_INTERVAL` to change how often the weather data is fetched.
- Add/remove cities to monitor in the `CITIES` list.
- Define alert thresholds in the `THRESHOLDS` dictionary.

### 7. Visualizations

The application generates visualizations using `matplotlib`. You can extend the `visualization.py` module to display temperature trends and weather summaries.

### 8. Testing

To run the unit tests, execute the following command:
```bash
python -m unittest discover tests/
```

## Features to Explore (Bonus)
- **Support for additional weather parameters**: Incorporate data like humidity, wind speed, and pressure.
- **Weather forecasts**: Fetch and display weather forecasts using the OpenWeatherMap forecast API.
- **Email alerts**: Implement an email alert system when thresholds are breached.

## Dependencies

- `requests`: For making API calls to OpenWeatherMap.
- `matplotlib`: For visualizing weather data and trends.
- `python-dotenv`: For managing environment variables.

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Future Enhancements
- **Database support**: Extend the storage system to use more sophisticated databases like PostgreSQL.
- **Notification system**: Add email or SMS notifications for weather alerts.
- **UI integration**: Develop a web or mobile interface for displaying weather data and alerts.



## Acknowledgments

- OpenWeatherMap API for providing weather data.
- **Your Name**: preethi.bttr@example.com
- **GitHub**: [Preethiseeram](https://github.com/Preethiseeram)
Repository Link:   https://github.com/Preethiseeram/rule-engine-ast.git

