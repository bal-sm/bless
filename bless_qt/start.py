from PySide6 import QtWidgets
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from bless_qt.duser.views import BlessWindow
from bless_qt.duser.views import bless_main_qml_path

import sys


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = BlessWindow()
    window.show()
    app.exec()


def main_qml():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(bless_main_qml_path())

    app.exec()
