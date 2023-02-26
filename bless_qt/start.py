from PySide6 import QtWidgets

from bless_qt.duser.views import BlessWindow

import sys


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = BlessWindow()
    window.show()
    app.exec()
