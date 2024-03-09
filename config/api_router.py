from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from reservamos_challenge.forecasts.api.views import ForecastViewSet
from reservamos_challenge.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("forecasts", ForecastViewSet, basename="forecasts")


app_name = "api"
urlpatterns = router.urls
