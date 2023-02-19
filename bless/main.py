from PySide6 import QtWidgets

from dquran.windows import BlessWindow

import sys

app = QtWidgets.QApplication(sys.argv)

window = BlessWindow()
window.show()
app.exec()
