from PySide6 import QtWidgets

import bismillah


class BismillahWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setWindowTitle("Read it")

        # Bismillaahirrahmaanirrahiim, table item
        self.bismillah_item = QtWidgets.QTableWidgetItem(bismillah.the_sentence)

        # Table configuration
        # Header and sider
        self.header = self.table.horizontalHeader()
        self.sider = self.table.verticalHeader()


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
