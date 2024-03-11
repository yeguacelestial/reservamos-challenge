from rest_framework import viewsets
from rest_framework.response import Response
from utils import openweather
from utils import reservamos


class ForecastViewSet(viewsets.ViewSet):
    def list(self, request):
        # TODO: use a serializer
        # 1. Read city
        city = request.query_params.get("city", None)

        response_data = {}
        if city:
            response_data = {"message": "City: " + city}

            # 2. Request city info on Reservamos API
            places = reservamos.get_places(city)

            # NOTE: This is very slow
            # 3. For each city:
            for place in places:
                latitude = place.get("lat", "")
                longitude = place.get("long", "")

                #   3.2 Request weather info for the next 7 days, from OpenWeather API
                place_weather = openweather.get_weather(
                    latitude=latitude,
                    longitude=longitude,
                )

                print("[D]", place_weather)

                #   3.3 Add weather info to the city properties
                daily = place_weather.get("daily", [])
                place["weather_forecast"] = {}
                for day in daily:
                    place["weather_forecast"][day["dt"]] = {
                        "min_temp": day["temp"]["min"],
                        "max_temp": day["temp"]["max"],
                    }

            # 4. Return cities names with min and max weather for the next 7 days
            response_data = places
        else:
            response_data = {"error": "City was not received"}

        return Response(response_data, status=200)
