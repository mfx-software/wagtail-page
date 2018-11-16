from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MySitesAppConfig(AppConfig):
    name = 'mysites'
    label = 'mysites'
    verbose_name = _("mysites")
