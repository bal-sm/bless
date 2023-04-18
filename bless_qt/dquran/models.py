import configparser
import os

from dquran.models import Ayatship
from dquran.models import Surat
from PySide6 import QtCore
from PySide6 import QtGui


def quran_model():
    AyatInQtRole = QtCore.Qt.UserRole + 1
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


def return_ayats(surat_name=None):
    # Harusnya pake id tapi ya udahlah gini aja dulu pake name
    if surat_name is None:
        # asalnya if surat_name == None:
        # but
        # bless_qt/dquran/models.py:57:19: E711 comparison to None should be 'if cond is None:'
        first_surat = Surat.objects.all().first()
        surat_name = first_surat.name

    ayatships = Ayatship.objects.filter(surat__name=surat_name)

    ayats = ""
    for ayatship in ayatships:
        ayats += ayatship.ayat.text
        ayats += " "
        ayat_number = convert_eng_num_to_ar_num(ayatship.number)
        ayats += ayat_number
        ayats += " "

    return ayats


def create_config_if_does_not_exist():
    path = "bless-qt_config.ini"

    if not os.path.isfile(path):
        config = configparser.ConfigParser()

        config.add_section("dquran")

        config.set("dquran", "font_size", "16")

        with open("bless-qt_config.ini", "w") as example:
            config.write(example)


def get_font_size_from_config():
    config_data = configparser.ConfigParser()
    config_data.read("bless-qt_config.ini")

    font_size = int(config_data["dquran"]["font_size"])

    return font_size


def write_font_size_to_config(font_size):
    config_data = configparser.ConfigParser()
    config_data.read("bless-qt_config.ini")

    config_data["dquran"]["font_size"] = str(font_size)

    with open("bless-qt_config.ini", "w") as example:
        config_data.write(example)


ar_num = "۰١٢٣٤٥٦٧٨٩"
eng_num = "0123456789"


def convert_eng_num_to_ar_num(the_numbers):
    table = str.maketrans(eng_num, ar_num)
    converted = str(the_numbers).translate(table)
    return converted


def get_last_window_width():
    config_data = configparser.ConfigParser()
    config_data.read("bless-qt_config.ini")

    if "dquran" not in config_data:
        config_data["dquran"] = {}

    if "window_width" not in config_data["dquran"]:
        config_data["dquran"]["window_width"] = "540"

    window_width = int(config_data["dquran"]["window_width"])

    return window_width


def save_last_window_width(width):
    config_data = configparser.ConfigParser()
    config_data.read("bless-qt_config.ini")

    if "dquran" not in config_data:
        config_data["dquran"] = {}

    config_data["dquran"]["window_width"] = str(width)

    with open("bless-qt_config.ini", "w") as example:
        config_data.write(example)
