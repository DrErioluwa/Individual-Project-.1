import tkinter as tk
from gui import WeatherApp
from utils import load_preferences, save_preferences
from logic import get_weather

def main():
    try:
        root = tk.Tk()
        root.title("Weather App")
        app = WeatherApp(root, load_preferences, save_preferences, get_weather)
        root.mainloop()
    except ImportError as e:
        print(f"Error: {e}")
        print("Please install the required modules using pip install -r requirements.txt")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()