import requests

def fetch_weather(api_key, location):
    """
    Fetch current weather data for the specified location using OpenWeatherMap API.
    """
    url = f"https://home.openweathermap.org/data/2.5/weather/?" 
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        print("Error fetching weather data:", data["message"])
        return None

def main():
    api_key = "4c03457d9fcc7e43903b3df1fdd26392"
    location = input("Enter city name or ZIP code: ")

    weather_data = fetch_weather(api_key, location)
    if weather_data:
        print("Current weather in", location)
        print("Temperature:", weather_data["temperature"], "°C")
        print("Humidity:", weather_data["humidity"], "%")
        print("Weather conditions:", weather_data["description"])
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()
