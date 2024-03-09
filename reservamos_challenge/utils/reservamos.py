import json

import requests

places_endpoint = "https://search.reservamos.mx/api/v2/places"


def get_places(querystring: str):
    response = requests.get(places_endpoint, params=querystring)
    response = json.loads(response.text)

    return response
