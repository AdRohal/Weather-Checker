import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data. Status code: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to fetch weather data.")

def main():
    # Replace 'YOUR_API_KEY' with the actual API key you obtained from OpenWeatherMap
    api_key = "YOUR_API_KEY"

    while True:
        city = input("Enter city name (type 'exit,' 'bye,' or 'cancel' to quit): ").lower()

        if city in ['exit', 'bye', 'cancel']:
            print("Goodbye!")
            break

        weather_data = get_weather(api_key, city)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
