import tkinter as tk
from tkinter import messagebox
from logic import get_weather
from utils import load_preferences, save_preferences

def search_weather():
    city = city_entry.get()
    if city:
        try:
            weather = get_weather(city)
            if weather:
                result_label.config(text=f"Temperature: {weather['temp']}°C\nDescription: {weather['description']}")
                try:
                    save_preferences(city)
                except Exception as e:
                    messagebox.showerror("Error", "Unable to save preferences")
            else:
                messagebox.showerror("Error", "Invalid weather data")
        except Exception as e:
            messagebox.showerror("Error", "Unable to fetch weather data")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def clear_fields():
    city_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
search_button = tk.Button(root, text="Search", command=search_weather)
search_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

try:
    root.mainloop()
except Exception as e:
    messagebox.showerror("Error", "An unexpected error occurred")