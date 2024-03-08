import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "reservamos_challenge.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import reservamos_challenge.users.signals  # noqa: F401
