import requests
import matplotlib.pyplot as plt

# API key and city name
api_key = "3e9abb9d7cde32a7f16dc80eebc34fa8"
city_name = "mumbai"

# Construct the API URL
forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&cnt=5&appid={api_key}"

# Send a request to OpenWeatherMap API
response = requests.get(forecast_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract data from the API response
    forecast_data = response.json()

    # Extract times and temperatures from the forecast data
    forecast_times = [entry['dt_txt'] for entry in forecast_data['list']]
    forecast_temperatures = [entry['main']['temp'] for entry in forecast_data['list']]

    # Plotting the data
    plt.figure(figsize=(10, 5))
    plt.plot(forecast_times, forecast_temperatures, marker='o', color='green')  # Plotting with a circular marker
    plt.title(f"Weather Forecast: {city_name}")
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing

    # Show the plot
    plt.show()

else:
    print(f"Request failed with status code: {response.status_code}")
