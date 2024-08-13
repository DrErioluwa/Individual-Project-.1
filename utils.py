import json
import os

PREFERENCES_FILE = 'data/preferences.json'

def save_preferences(city):
    if not isinstance(city, str) or not validate_city(city):
        raise ValueError("Invalid city name")
    try:
        os.makedirs(os.path.dirname(PREFERENCES_FILE), exist_ok=True)
        with open(PREFERENCES_FILE, 'w') as f:
            json.dump({'city': city}, f)
    except OSError as e:
        raise RuntimeError(f"Unable to save preferences: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def load_preferences():
    try:
        if os.path.exists(PREFERENCES_FILE):
            with open(PREFERENCES_FILE, 'r') as f:
                data = json.load(f)
                return data.get('city', '')
        return ''
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON data: {e}")
    except OSError as e:
        raise RuntimeError(f"Unable to load preferences: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def validate_city(city):
    return bool(city) and len(city) <= 50

# Example usage
if __name__ == "__main__":
    city = "Lagos"
    try:
        save_preferences(city)
        last_searched_city = load_preferences()
        print(f"Last searched city: {last_searched_city}")
    except RuntimeError as e:
        print(f"Error: {e}")