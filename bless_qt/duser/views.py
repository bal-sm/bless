from PySide6 import QtWidgets

from bless_qt.dquran.views import BismillahWindow, QuranWindow


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
