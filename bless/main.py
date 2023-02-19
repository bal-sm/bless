from PySide6 import QtWidgets

from duser.views import BlessWindow

import sys

app = QtWidgets.QApplication(sys.argv)

window = BlessWindow()
window.show()
app.exec()
