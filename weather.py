import requests


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("\nCould not look up location")
        return None

    data = response.json()
    if "results" not in data:
        print(f"\nNo match found for {city}\n")
        return None

    place = data["results"][0]
    return place["name"], place.get("admin1", ""), place["latitude"], place["longitude"], place["timezone"]


def get_weather(latitude, longitude, timezone):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "precipitation_probability_max,temperature_2m_max,temperature_2m_min",
        "current": "temperature_2m,rain,showers,snowfall",
        "timezone": timezone,
        "forecast_days": 1,
        "wind_speed_unit": "mph",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch",
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("\nCould not retrieve weather")
        print(f"Status code: {response.status_code}\n")
        return None

    return response.json()


def parsed_data(latitude, longitude, timezone):
    data = get_weather(latitude, longitude, timezone)
    if data is None:
        return None
    
    current_temp = data["current"]["temperature_2m"]
    rain = data["current"]["rain"]
    showers = data["current"]["showers"]
    snow = data["current"]["snowfall"]
    chance_of_rain = data["daily"]["precipitation_probability_max"][0]
    high_temp = data["daily"]["temperature_2m_max"][0]
    low_temp = data["daily"]["temperature_2m_min"][0]
    return current_temp, rain, showers, snow, chance_of_rain, high_temp, low_temp

def main():
    city = input("\nEnter a city: ")
    location = get_coordinates(city)
    if location is None:
        return

    location_name, state, latitude, longitude, timezone = location

    results = parsed_data(latitude, longitude, timezone)
    if results is None:
        return
    current_temp, rain, showers, snow, chance_of_rain, high_temp, low_temp = results

    print(f"\nWeather for {location_name}, {state}")
    print(f"\nCurrent Temperature: {current_temp}°F")
    if rain > 0 or showers > 0:
        print("It is raining")
    if snow > 0:
        print("it is snowing")
    print(f"Chance of rain: {chance_of_rain}%")
    print(f"High for the day: {high_temp}°F")
    print(f"Low for the day: {low_temp}°F\n")

main()




    






