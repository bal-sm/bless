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
from bless_qt.dquran.models import create_config_if_does_not_exist
from bless_qt.dquran.models import get_font_size_from_config
from bless_qt.dquran.models import write_font_size_to_config
from bless_qt.dquran.models import get_last_window_width
from bless_qt.dquran.models import save_last_window_width
from bless_qt.dquran.views import quran_main_qml_path
from bless_qt.duser.views import bless_main_qml_path

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
        if s == 0:
            create_config_if_does_not_exist()
            size = get_font_size_from_config()
            return size
        else:
            size = int(s * 34)
            write_font_size_to_config(size)
            if size <= 0:
                return 1
            else:
                return size

    @Slot(float, result=float)
    def returnSliderValueFromConfig(self, s):
        font_size = get_font_size_from_config()
        slider_value = int(font_size) / 34
        return slider_value

    @Slot(result=int)
    def getLastWindowWidth(self):
        create_config_if_does_not_exist()
        window_width = get_last_window_width()
        return window_width

    @Slot(int)
    def saveLastWindowWidth(self, width):
        save_last_window_width(width)


if __name__ == "__main__":
    qurans = quran_model()
    surats = surat_model()

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("quranmodel", qurans)
    engine.rootContext().setContextProperty("suratModel", surats)
    engine.load(bless_main_qml_path())

    app.exec()
