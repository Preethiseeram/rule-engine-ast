import matplotlib.pyplot as plt

class WeatherVisualization:
    def plot_temperature_trends(self, city, temperatures):
        plt.plot(temperatures)
        plt.title(f"Temperature Trends for {city}")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.show()
