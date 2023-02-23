from PySide6 import QtWidgets

from dquran.views import BismillahWindow


class BlessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bless")
        self.button = QtWidgets.QPushButton("Mulai", self)
        self.button.clicked.connect(self.bismillah_window)
        self.setCentralWidget(self.button)

    def bismillah_window(self):
        self.w = BismillahWindow()
        self.w.table.show()
        self.hide()
