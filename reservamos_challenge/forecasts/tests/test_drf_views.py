import pytest
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

from reservamos_challenge.forecasts.api.views import ForecastViewSet
from django.contrib.auth.models import AnonymousUser


class TestForecastViewSet:
    @pytest.fixture()
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_list(self, user: AnonymousUser, api_rf: APIRequestFactory):
        view = ForecastViewSet()
        request = api_rf.get("/api/forecasts/", {"city": "monterrey"})

        request.user = user

        request = Request(request)

        view.request = request

        response = view.list(request)

        assert response.status_code == 200
