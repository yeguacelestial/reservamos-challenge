from concurrent.futures import ThreadPoolExecutor
from rest_framework import viewsets
from rest_framework.response import Response
from utils import openweather
from utils import reservamos


class ForecastViewSet(viewsets.ViewSet):
    def list(self, request):
        city = request.query_params.get("city", None)

        response_data = {}
        if city:
            # Request city info on Reservamos API
            places = reservamos.get_places(city)

            with ThreadPoolExecutor() as executor:
                # For each city, create a task to fetch weather info:
                future_weather = {
                    executor.submit(
                        openweather.get_weather,
                        place.get("lat", ""),
                        place.get("long", ""),
                    ): place
                    for place in places
                }

                for future in future_weather:
                    place = future_weather[future]
                    place_weather = future.result()

                    if "daily" in place_weather:
                        weather_forecast = {}

                        for day in place_weather["daily"]:
                            weather_forecast[day["dt"]] = {
                                "min_temp": day["temp"]["min"],
                                "max_temp": day["temp"]["max"],
                            }
                        place["weather_forecast"] = weather_forecast

                response_data["places"] = places

        else:
            response_data["error"] = "City was not received"

        return Response(response_data, status=200)
