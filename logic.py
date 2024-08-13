import requests

API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        print("Error: Could not fetch weather data")
        return None

if __name__ == "__main__":
    city = "Lagos"
    weather = get_weather(city)
    if weather:
        print(f"Temperature: {weather['temp']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("No weather data available")
