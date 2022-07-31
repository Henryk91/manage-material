# Settings for local development environment
from .base import *  # noqa
from .base import env
# from .constants import *  # noqa


DEFAULT_FROM_EMAIL = "webmaster@localhost"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# whitenoise needs to be at the top
INSTALLED_APPS = ["whitenoise.runserver_nostatic", "debug_toolbar"] + INSTALLED_APPS  # noqa
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE  # noqa

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]

# domain with port to properly work on local development
BACKEND_DOMAIN = "0.0.0.0:8000"

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

SWAGGER_ENABLED = True
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda r: False, "RESULTS_CACHE_SIZE": 100}
