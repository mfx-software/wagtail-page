# Imported for historical reasons
from wagtail import __semver__, __version__  # noqa

default_app_config = 'core.apps.CoreAppConfig'


def setup():
    import warnings
    from wagtail.utils.deprecation import removed_in_next_version_warning

    warnings.simplefilter("default", removed_in_next_version_warning)


setup()
