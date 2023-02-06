from PySide6 import QtWidgets

import sys

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("Bless")

button = QtWidgets.QPushButton()
button.setText("Mulai")

window.setCentralWidget(button)

window.show()
app.exec()
