# main.py

import tkinter as tk
from gui import WeatherApp

def main():
    root = tk.Tk()
    root.title("Weather App")
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
