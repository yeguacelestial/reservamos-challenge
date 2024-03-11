import json

import requests
from django.conf import settings


def get_weather(latitude: str, longitude: str):
    onecall_endpoint = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&appid={settings.OPENWEATHER_API_KEY}"
    response = requests.get(onecall_endpoint)
    response = json.loads(response.text)

    return response


def get_weather_bulk(latitudes, longitudes):
    endpoint = "https://api.openweathermap.org/data/2.5/onecall"
    api_key = settings.OPENWEATHER_API_KEY
    params = {
        "lat": ",".join(map(str, latitudes)),
        "lon": ",".join(map(str, longitudes)),
        "appid": api_key,
    }

    response = requests.get(endpoint, params=params)
    response_data = json.loads(response.text)

    print("[D] openweather.get_weather_bulk: ", response_data)
    # Ensure the response is a list, if not, return an empty list
    if not isinstance(response_data, list):
        return []

    return response_data
