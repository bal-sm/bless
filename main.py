from PySide6 import QtWidgets

import sys


class BlessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bless")
        button = QtWidgets.QPushButton("Mulai")

        self.setCentralWidget(button)


app = QtWidgets.QApplication(sys.argv)

window = BlessWindow()
window.show()
app.exec()
