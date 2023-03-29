import os
import sys

import django
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bless_server.settings")

django.setup()

# noreorder
from bless_qt.dquran.models import quran_model
from bless_qt.dquran.views import quran_main_qml_path

if __name__ == "__main__":
    qurans = quran_model()

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("quranmodel", qurans)
    engine.load(quran_main_qml_path())

    app.exec()
