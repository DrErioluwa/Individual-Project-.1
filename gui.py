# gui.py

import tkinter as tk
from tkinter import messagebox
from logic import get_weather
from utils import load_preferences, save_preferences

def create_gui():
    def search_weather():
        city = city_entry.get()
        if city:
            try:
                weather = get_weather(city)
                result_label.config(text=f"Temperature: {weather['temp']}°C\nDescription: {weather['description']}")
                save_preferences(city)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")

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

    root.mainloop()

if __name__ == '__main__':
    create_gui()
