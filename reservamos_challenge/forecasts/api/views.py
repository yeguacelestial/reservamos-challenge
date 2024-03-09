from rest_framework import viewsets
from rest_framework.response import Response
from utils import openweather
from utils import reservamos


class ForecastViewSet(viewsets.ViewSet):
    def list(self, request):
        # TODO: use a serializer
        city = request.query_params.get("city", None)

        response_data = {}
        if city:
            # 1. Read city
            response_data = {"message": "City: " + city}

            # 2. Request city info on Reservamos API
            places = reservamos.get_places(city)

            # 3. For each city:
            for place in places:
                latitude = place.get("lat", "")
                longitude = place.get("long", "")

                # NOTE: This is very slow
                #   TODO: 3.2 Request weather info for the next 7 days, from OpenWeather API
                place_weather = openweather.get_weather(
                    latitude=latitude,
                    longitude=longitude,
                )

                daily = place_weather.get("daily", "")
                # first min and max:
                # daily[0]["temp"]["min"]
                # daily[0]["temp"]["max"]
            #   3.3 Add weather info to the city properties
            # 4. Return cities names with min and max weather for the next 7 days

        else:
            response_data = {"error": "City was not received"}

        return Response(response_data, status=400)
