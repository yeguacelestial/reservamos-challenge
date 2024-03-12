from concurrent.futures import ThreadPoolExecutor

from rest_framework import viewsets
from rest_framework.response import Response

from reservamos_challenge.utils import openweather, reservamos

from reservamos_challenge.forecasts.api.serializers import CitySerializer


class ForecastViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = CitySerializer(data=request.query_params)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        city = serializer.validated_data["city"]

        if city:
            # Request city info on Reservamos API
            places = reservamos.get_places(city)

            if len(places) == 0:
                return Response({"message": "no places were found"}, status=404)

            with ThreadPoolExecutor() as executor:
                # For each city, create a task to fetch weather info:
                future_weather = {
                    executor.submit(
                        openweather.get_weather_with_cache,
                        place.get("lat", ""),
                        place.get("long", ""),
                    ): place
                    for place in places
                }

                for future in future_weather:
                    place = future_weather[future]

                    try:
                        place_weather = future.result(timeout=10)  # 10-second timeout
                    except TimeoutError:
                        place_weather = {}

                    if "daily" in place_weather:
                        weather_forecast = {}

                        for day in place_weather["daily"]:
                            weather_forecast[day["dt"]] = {
                                "min_temp": day["temp"]["min"],
                                "max_temp": day["temp"]["max"],
                            }
                        place["weather_forecast"] = weather_forecast

                return Response(places, status=200)

        else:
            return Response({"error": "no city received"}, status=400)
