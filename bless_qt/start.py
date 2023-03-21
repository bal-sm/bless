import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from bless_qt.dquran.models import quran_model
from bless_qt.duser.views import bless_main_qml_path
from bless_qt.duser.views import BlessWindow


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = BlessWindow()
    window.show()
    app.exec()


def main_qml():
    qurans = quran_model()

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("quranmodel", qurans)
    engine.load(bless_main_qml_path())

    app.exec()
