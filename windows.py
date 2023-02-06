from PySide6 import QtWidgets


class BlessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bless")
        button = QtWidgets.QPushButton("Mulai")

        self.setCentralWidget(button)
