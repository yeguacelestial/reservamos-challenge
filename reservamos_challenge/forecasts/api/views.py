from rest_framework import viewsets
from rest_framework.response import Response


class ForecastViewSet(viewsets.ViewSet):
    def list(self, request):
        city = request.query_params.get("city", None)

        response_data = {}
        if city:
            response_data = {"message": "City: " + city}

        else:
            response_data = {"error": "City was not received"}

        return Response(response_data, status=400)
