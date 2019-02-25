"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""
from channels.routing import get_default_application

import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
django.setup()

application = get_default_application()
