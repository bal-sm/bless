import os
import sys

import django
from PySide6.QtCore import QObject
from PySide6.QtCore import Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QmlElement
from PySide6.QtQml import QQmlApplicationEngine

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bless_server.settings")

django.setup()

# noreorder
from bless_qt.dquran.models import surat_model
from bless_qt.dquran.models import quran_model
from bless_qt.dquran.models import return_ayats
from bless_qt.dquran.views import quran_main_qml_path

QML_IMPORT_NAME = "md.ayatproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Bridge(QObject):
    @Slot(str, result=str)
    def getAyatsForSurat(self, s):
        ayats = return_ayats(s)
        return ayats

    @Slot(float, result=int)
    def getSize(self, s):
        size = int(s * 34)
        if size <= 0:
            return 1
        else:
            return size


if __name__ == "__main__":
    qurans = quran_model()
    surats = surat_model()

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("quranmodel", qurans)
    engine.rootContext().setContextProperty("suratModel", surats)
    engine.load(quran_main_qml_path())

    app.exec()
