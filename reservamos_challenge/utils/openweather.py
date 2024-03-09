import json

import requests
from django.conf import settings


def get_weather(latitude: str, longitude: str):
    onecall_endpoint = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&appid={settings.OPENWEATHER_API_KEY}"
    response = requests.get(onecall_endpoint)
    response = json.loads(response.text)

    return response
