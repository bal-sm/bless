from dquran.models import Ayatship
from PySide6 import QtCore
from PySide6 import QtGui

AyatInQtRole = QtCore.Qt.UserRole + 1


def quran_model():
    model = QtGui.QStandardItemModel()
    model.setItemRoleNames({AyatInQtRole: b"ayatinqt"})

    ayatships = Ayatship.objects.all()

    for ayat in ayatships:
        it = QtGui.QStandardItem()
        it.setData(ayat.ayat.text, AyatInQtRole)
        model.appendRow(it)

    return model
