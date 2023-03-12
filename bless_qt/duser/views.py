from PySide6 import QtWidgets
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from bless_qt.dquran.views import BismillahWindow, QuranWindow

import os


class BlessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bless")
        self.button = QtWidgets.QPushButton("Mulai", self)
        self.button.clicked.connect(self.quran_window)
        self.setCentralWidget(self.button)

    def bismillah_window(self):
        self.w = BismillahWindow()
        self.w.table.show()
        self.hide()

    def quran_window(self):
        self.w = QuranWindow()
        self.w.table.show()
        self.hide()


def bless_main_qml_path():
    return os.path.join(os.path.dirname(__file__), "qml/main.qml")
