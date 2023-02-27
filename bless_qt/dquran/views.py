from PySide6 import QtWidgets

from bismillah_on_py import bismillah

from dquran.models import Ayatship


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

        # Hide them
        self.header.hide()
        self.sider.hide()

        # Set row, column, and item
        self.table.setRowCount(1)
        self.table.setColumnCount(1)
        self.table.setItem(0, 0, self.bismillah_item)
        self.table.resizeColumnsToContents()

        # Set maximum width and height
        self.table.setMaximumWidth(self.header.length())
        self.table.setMaximumHeight(self.sider.length())


class AnNasAyat1Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setWindowTitle("Read it")

        self.item = Ayatship.objects.get(surat__number=114, number=1)

        # Bismillaahirrahmaanirrahiim, table item
        self.bismillah_item = QtWidgets.QTableWidgetItem(self.item.ayat.text)

        # Table configuration
        # Header and sider
        self.header = self.table.horizontalHeader()
        self.sider = self.table.verticalHeader()

        # Hide them
        self.header.hide()
        self.sider.hide()

        # Set row, column, and item
        self.table.setRowCount(1)
        self.table.setColumnCount(1)
        self.table.setItem(0, 0, self.bismillah_item)
        self.table.resizeColumnsToContents()

        # Set maximum width and height
        self.table.setMaximumWidth(self.header.length())
        self.table.setMaximumHeight(self.sider.length())
