from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreAppConfig(AppConfig):
    name = 'core'
    label = 'core'
    verbose_name = _("core")

    def ready(self):
        from wagtail.core.signal_handlers import register_signal_handlers
        register_signal_handlers()
