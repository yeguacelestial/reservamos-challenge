import json

import requests
from django.conf import settings

from django.core.cache import cache


def get_weather(latitude: str, longitude: str, units: str = "metric"):
    onecall_endpoint = f"https://api.openweathermap.org/data/2.5/onecall?units={units}&lat={latitude}&lon={longitude}&appid={settings.OPENWEATHER_API_KEY}&exclude=current,minutely,hourly"
    response = requests.get(onecall_endpoint)
    response = json.loads(response.text)
    return response


def get_weather_with_cache(latitude: str, longitude: str):
    cache_key = f"weather_{latitude}_{longitude}"
    weather_data = cache.get(cache_key)

    if weather_data is None:
        place_weather = get_weather(latitude, longitude)
        if place_weather and "daily" in place_weather:
            weather_forecast = {}
            for day in place_weather["daily"]:
                weather_forecast[day["dt"]] = {
                    "min_temp": day["temp"]["min"],
                    "max_temp": day["temp"]["max"],
                }
            # Save weather data to cache for 1 hour
            cache.set(cache_key, weather_forecast, timeout=3600)
            return place_weather
        else:
            return {}
    else:
        return weather_data
