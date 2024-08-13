import json
import os

PREFERENCES_FILE = 'data/preferences.json'

def save_preferences(city):
    os.makedirs(os.path.dirname(PREFERENCES_FILE), exist_ok=True)
    with open(PREFERENCES_FILE, 'w') as f:
        json.dump({'city': city}, f)

def load_preferences():
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, 'r') as f:
            data = json.load(f)
            return data.get('city', '')
    return ''

def validate_city(city):
    return bool(city) and len(city) <= 50

# Example usage
if __name__ == "__main__":
    city = "Lagos"
    save_preferences(city)
    last_searched_city = load_preferences()
    print(f"Last searched city: {last_searched_city}")
