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
            response_data = {"message": "City: " + city}

            # Request city info on Reservamos API
            places = reservamos.get_places(city)

            latitudes = []
            longitudes = []

            # For each city:
            for place in places:
                latitude = place.get("lat", "")
                longitude = place.get("long", "")

                latitudes.append(latitude)
                longitudes.append(longitude)

            # Make a single call to OpenWeatherMap for all places
            all_weather = openweather.get_weather_bulk(latitudes, longitudes)

            for i, place in enumerate(places):
                latitude = place.get("lat", "")
                longitude = place.get("long", "")

                # Ensure all_weather has data and has the same length as places
                if i < len(all_weather):
                    place_weather = all_weather[i]
                else:
                    # Handle the case where all_weather doesn't have enough data
                    place_weather = {}

                daily_weather = place_weather.get("daily", [])

                if daily_weather:
                    # Simplify the data to just min/max temp for each day
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
