import os

from bismillah_on_py import bismillah
from dquran.models import Ayatship
from PySide6 import QtWidgets


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


class QuranWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setWindowTitle("Read it")

        # Table configuration
        # Header and sider
        self.header = self.table.horizontalHeader()
        self.sider = self.table.verticalHeader()

        # Hide them
        self.header.hide()
        self.sider.hide()

        # Get all Ayatship queries from django
        self.ayatships = Ayatship.objects.all()

        # Set row, column, and item
        self.table.setRowCount(1)
        self.table.setColumnCount(self.ayatships.count())

        # Set item
        for i, ayatsh in enumerate(self.ayatships):
            self.ayat_text = QtWidgets.QTableWidgetItem(ayatsh.ayat.text)
            self.table.setItem(0, i, self.ayat_text)

        self.table.resizeColumnsToContents()

        # Set maximum width and height
        self.table.setMaximumWidth(self.header.length())
        self.table.setMaximumHeight(self.sider.length())

        # Set smooth horizontal scroll
        self.table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)


def quran_main_qml_path():
    return os.path.join(os.path.dirname(__file__), "qml/main.qml")
