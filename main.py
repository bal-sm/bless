import django
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bless_server.settings")

django.setup()

from bless_qt import start


def main():
    start.main()


def main_qml():
    start.main_qml()


if __name__ == "__main__":
    main_qml()
