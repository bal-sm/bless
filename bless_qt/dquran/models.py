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
    SuratInQtRole = QtCore.Qt.UserRole + 2
    model = QtGui.QStandardItemModel()
    model.setItemRoleNames({SuratInQtRole: b"suratinqt"})
    # ayo kita lihat apa bisa kalo ga di set dulu item role names nya

    surats = Surat.objects.all()

    for surat in surats:
        it = QtGui.QStandardItem()
        it.setData(surat.name, SuratInQtRole)
        # Soalnya kan ada string method tea, terus jadi gampang id nya.
        model.appendRow(it)

    return model
    # Ya Allah swt., this set of backend and frontend is the best. Thank you for utusan-Mu (saw.) ya Rabb-ku


def get_surat_specific_with_name(surat_name):
    # Harusnya pake id tapi ya udahlah gini aja dulu pake name
    AyatInQtRole = QtCore.Qt.UserRole + 3
    model = QtGui.QStandardItemModel()
    model.setItemRoleNames({AyatInQtRole: b"ayatinqt"})
    ayatships = Ayatship.objects.filter(surat__name=surat_name)

    for ayat in ayatships:
        it = QtGui.QStandardItem()
        it.setData(ayat.ayat.text, AyatInQtRole)
        model.appendRow(it)

    return model
