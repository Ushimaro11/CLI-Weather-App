import requests


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("\nCould not reach the server")
        return None

    if response.status_code != 200:
        print("\nCould not look up location")
        return None

    data = response.json()
    if "results" not in data:
        print(f"\nNo match found for {city}\n")
        return None

    place = data["results"][0]
    return place["name"], place.get("admin1", ""), place["latitude"], place["longitude"], place["timezone"], place.get("country_code", "")


def get_weather(latitude, longitude, timezone, country_code):
    if country_code == "US":
        temp_unit = "fahrenheit"
    else:
        temp_unit = "celsius"

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "precipitation_probability_max,temperature_2m_max,temperature_2m_min",
        "current": "temperature_2m,rain,showers,snowfall",
        "timezone": timezone,
        "forecast_days": 1,
        "wind_speed_unit": "mph",
        "temperature_unit": temp_unit,
        "precipitation_unit": "inch",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("\nCould not reach the server")
        return None
    
    if response.status_code != 200:
        print("\nCould not retrieve weather")
        print(f"Status code: {response.status_code}\n")
        return None

    return response.json()


def parsed_data(latitude, longitude, timezone, country_code):
    data = get_weather(latitude, longitude, timezone, country_code)
    if data is None:
        return None
    
    current_temp = data["current"]["temperature_2m"]
    rain = data["current"]["rain"]
    showers = data["current"]["showers"]
    snow = data["current"]["snowfall"]
    chance_of_rain = data["daily"]["precipitation_probability_max"][0]
    high_temp = data["daily"]["temperature_2m_max"][0]
    low_temp = data["daily"]["temperature_2m_min"][0]
    temp_format = data["current_units"]["temperature_2m"]
    return current_temp, rain, showers, snow, chance_of_rain, high_temp, low_temp, temp_format

def main():
    city = input("\nEnter a city: ")
    location = get_coordinates(city)
    if location is None:
        return

    location_name, state, latitude, longitude, timezone, country_code = location

    results = parsed_data(latitude, longitude, timezone, country_code)
    if results is None:
        return
    current_temp, rain, showers, snow, chance_of_rain, high_temp, low_temp, temp_format = results

    if state:
        place_name = f"{location_name}, {state}"
    else:
        place_name = location_name

    is_raining = rain > 0 or showers > 0
    is_snowing = snow > 0
    
    print(f"\nWeather for {place_name}")
    print(f"\nCurrent Temperature: {current_temp}{temp_format}")
    if is_raining and is_snowing:
        print("Currently raining and snowing")
    elif is_raining:
        print("Currently raining")
    elif is_snowing:
        print("Currently snowing")
    print(f"Chance of rain: {chance_of_rain}%")
    print(f"High for the day: {high_temp}{temp_format}")
    print(f"Low for the day: {low_temp}{temp_format}\n")

if __name__ == "__main__":
    main()