import django
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bless_server.settings")

django.setup()

from bless_qt import main
