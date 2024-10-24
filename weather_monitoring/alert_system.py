class WeatherAlertSystem:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def check_alert(self, processed_data):
        if processed_data["temperature"] > self.thresholds["temperature"]:
            print(f"ALERT: Temperature exceeded threshold in {processed_data['city']}")
