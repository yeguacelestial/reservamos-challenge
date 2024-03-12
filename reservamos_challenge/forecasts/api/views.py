from rest_framework import viewsets
from rest_framework.response import Response
from utils import openweather
from utils import reservamos


class ForecastViewSet(viewsets.ViewSet):
    def list(self, request):
        city = request.query_params.get("city", None)

        response_data = {}
        if city:
            response_data = {"message": "City: " + city}

            # Request city info on Reservamos API
            places = reservamos.get_places(city)

            # For each city:
            for place in places:
                latitude = place.get("lat", "")
                longitude = place.get("long", "")

                place_weather = openweather.get_weather(latitude, longitude)
                daily_weather = place_weather.get("daily", [])

                if daily_weather:
                    weather_forecast = {}

                    for day in daily_weather:
                        weather_forecast[day["dt"]] = {
                            "min_temp": day["temp"]["min"],
                            "max_temp": day["temp"]["max"],
                        }
                    place["weather_forecast"] = weather_forecast

            response_data["places"] = places

        else:
            response_data["error"] = "City was not received"

        return Response(response_data, status=200)
