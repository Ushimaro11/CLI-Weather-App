# CLI Weather App

A lightweight Python command-line tool that fetches real-time weather conditions and daily forecasts for any city using the [Open-Meteo API](https://open-meteo.com/)—no API key required.

## Features

- **City Geocoding:** Converts any city name into exact latitude, longitude, and local timezone coordinates.
- **Current Conditions:** Displays live temperature (°F) and active precipitation alerts (rain, showers, or snow).
- **Daily Forecast:** Shows the daily high, daily low, and maximum chance of precipitation.
- **Zero-Auth Setup:** Uses Open-Meteo's free public endpoints, so it runs immediately without managing `.env` files or API tokens.

## Prerequisites

- Python 3.8 or higher
- `requests` library

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/cli-weather-app.git](https://github.com/yourusername/cli-weather-app.git)
   cd cli-weather-app
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows
   python -m venv .venv
   .venv\Scripts\activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```bash
   python weather.py
   ```

## Example Output

```text
Enter a city: Wichita

Weather for Wichita, Kansas

Current Temperature: 64.2°F
Chance of rain: 10%
High for the day: 68.5°F
Low for the day: 45.1°F
```

## How It Works

1. `get_coordinates(city)` queries the Open-Meteo Geocoding API to resolve the city name into coordinates and a local timezone.
2. `get_weather(latitude, longitude, timezone)` fetches current weather metrics and the 1-day forecast in Imperial units (`°F`, `mph`, `inch`).
3. `parsed_data(...)` extracts the relevant fields and passes them to `main()` for formatted terminal output.
