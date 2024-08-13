try:
    import requests
except ImportError:
    print("Error: The 'requests' module is not installed. Please install it using 'pip install requests'.")
    exit(1)  # Exit the script if the module is not available
import requests
try:
    API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
    if not API_KEY:
        raise ValueError("API key is not provided. Please set the API_KEY variable with your OpenWeatherMap API key.")
except ValueError as ve:
    print(f"Error: {ve}")
    exit(1)

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    if not city:
        print("Error: City name cannot be empty.")
        return None

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        weather = {
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif response.status_code == 404:
            print("Error: City not found. Please check the city name.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Could not fetch weather data. {req_err}")
    except ValueError as json_err:
        print(f"Error: Could not parse JSON response. {json_err}")
    return None

if __name__ == "__main__":
    city = "Lagos"
    weather = get_weather(city)
    if weather:
        print(f"Temperature: {weather['temp']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("No weather data available")