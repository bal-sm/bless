from dquran.models import Ayatship
from dquran.models import Surat
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


def surat_model():
    model = QtGui.QStandardItemModel()
    # model.setItemRoleNames({AyatInQtRole: b"ayatinqt"})
    # ayo kita lihat apa bisa kalo ga di set dulu item role names nya

    surats = Surat.objects.all()

    for surat in surats:
        it = QtGui.QStandardItem()
        it.setData(surat)
        # Soalnya kan ada string method tea, terus jadi gampang id nya.
        model.appendRow(it)

    return model
    # Ya Allah swt., this set of backend and frontend is the best. Thank you for utusan-Mu (saw.) ya Rabb-ku
