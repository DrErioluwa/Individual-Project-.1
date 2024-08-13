# Simple Weather App

This is a desktop weather application that allows you to check the current weather for any city.

## Setup and Running the Application

1. Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. Open a terminal or command prompt.

3. Navigate to the folder containing the application files.

4. Set up a virtual environment (optional but recommended):
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

5. Install the required packages:
Certainly. Here's a simple and descriptive README file for your weather application:
markdownCopy# Simple Weather App

This is a desktop weather application that allows you to check the current weather for any city.

## Setup and Running the Application

1. Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. Open a terminal or command prompt.

3. Navigate to the folder containing the application files.

4. Set up a virtual environment (optional but recommended):
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

5. Install the required packages:
pip install requests

6. Get an API key:
- Go to [OpenWeatherMap](https://openweathermap.org/) and create a free account.
- Once logged in, go to your API keys and copy your key.
- Open the `logic.py` file and replace `"YOUR_API_KEY_HERE"` with your actual API key.

7. Run the application:
python main.py


## How to Use

1. When the application opens, you'll see a window with a text box.

2. Type the name of a city in the text box.

3. Click the "Search" button or press Enter.

4. The current temperature and weather description for that city will appear below.

5. The application remembers the last city you searched for and will show it when you reopen the app.

## Troubleshooting

- If you get an error message, make sure you've entered a valid city name and that you have an internet connection.
- If the application doesn't start, ensure you've followed all the setup steps correctly.

For any other issues, please contact the developer.

