# CLI Weather App

A lightweight Python command-line tool that fetches real-time weather conditions and daily forecasts for any city worldwide using the [Open-Meteo API](https://open-meteo.com/)—no API key required.

## Features

- **City Geocoding:** Converts any city name into exact latitude, longitude, local timezone, and country code coordinates.
- **Automatic Unit Localization:** Detects the country code and automatically displays temperatures in Fahrenheit (`°F`) for US locations and Celsius (`°C`) for international locations.
- **Current Conditions:** Displays live temperature and active precipitation alerts (rain, snow, or wintry mix).
- **Daily Forecast:** Shows the daily high, daily low, and maximum chance of precipitation.
- **Resilient & Zero-Auth:** Built with request timeouts and network error handling, using Open-Meteo's free public endpoints without `.env` files or API tokens.

## Prerequisites

- Python 3.8 or higher
- `requests` library

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ushimaro11/cli-weather-app.git](https://github.com/Ushimaro11/cli-weather-app.git)
   cd cli-weather-app
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .venv\Scripts\Activate.ps1
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

**US Location (Fahrenheit):**
```text
Enter a city: Chicago

Weather for Chicago, Illinos

Current Temperature: 64.2°F
Chance of rain: 10%
High for the day: 68.5°F
Low for the day: 45.1°F
```

**International Location (Celsius):**
```text
Enter a city: Tokyo

Weather for Tokyo, Tokyo

Current Temperature: 14.8°C
Currently raining
Chance of rain: 80%
High for the day: 16.2°C
Low for the day: 9.4°C
```

## How It Works

1. `get_coordinates(city)` queries the Open-Meteo Geocoding API to resolve the city name into coordinates, region/state, local timezone, and ISO `country_code`.
2. `get_weather(latitude, longitude, timezone, country_code)` selects `"fahrenheit"` for `"US"` locations or `"celsius"` otherwise, then fetches current weather metrics and the 1-day forecast.
3. `parsed_data(...)` extracts the weather metrics along with the API-provided `temperature_2m` unit symbol (`°F` or `°C`) and returns them to `main()` for formatted terminal output.