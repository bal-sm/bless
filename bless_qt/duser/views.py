from PySide6 import QtWidgets

from bless_qt.dquran.views import BismillahWindow, AnNasAyat1Window


class BlessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bless")
        self.button = QtWidgets.QPushButton("Mulai", self)
        self.button.clicked.connect(self.annas_ayat1_window)
        self.setCentralWidget(self.button)

    def bismillah_window(self):
        self.w = BismillahWindow()
        self.w.table.show()
        self.hide()

    def annas_ayat1_window(self):
        self.w = AnNasAyat1Window()
        self.w.table.show()
        self.hide()
