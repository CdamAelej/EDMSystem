import os.path
import sys
import database
import sqlalchemy
from edms_box import Ui_ECDS_form
from PyQt5 import QtWidgets, QtCore
from sqlalchemy import *
from sqlalchemy.orm import *


# class BDelegat(QtWidgets.QStyledItemDelegate):


class GlowneOkno(QtWidgets.QMainWindow, Ui_ECDS_form):
    def __init__(self):
        super(GlowneOkno, self).__init__()
        self.setupUi(self)
        self.pokazPracownikow_action.triggered.connect(lambda: self.zaladujPracownikow())

    # Python mowi propert. Python mondry byc XD
    """def polaczenieBazy(self):
        bazaDanych = QtSql.QSqlDatabase("bazafirmy.sqlite")
        #plik = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bazafirmy.sqlite")
        bazaDanych.setDatabaseName(bazaDanych)
        if not bazaDanych.open():
            QtWidgets.QMessageBox.critical(
                None,
                QtWidgets.qApp.tr("Nie mozna otworzyc bazy"),
                QtWidgets.qApp.tr(
                    "Nie można stworzyc stabilnego polaczenia z baza danych"
                ),
                QtWidgets.QMessageBox.Cancel
            )
            return False
        return True"""

    def zaladujPracownikow(self,):
        Sesja = sessionmaker(bind=database.engine)
        sesja = Sesja()
        sw = self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()
        sw.resize(640, 480)
        tabela = self.tableView
        tabela.horizontalHeader().setStretchLastSection(True)
        tabela.setWordWrap(True)
        tabela.setTextElideMode(QtCore.Qt.ElideLeft)
        selekcja = select(database.Pracownik)
        wyniki = engine.connect().execute(selekcja)
        for wiersz in wyniki:
            print(wiersz)
        """for s in sesja.query(database.Pracownik).all():
            print(str(s.IDpracownika), str(s.Imie), str(s.Nazwisko), str(s.DataUrodzenia), str(s.su))"""
        #tabela.setItemDelegateForColumn()
        #model = sesja.query(database.Pracownik).all()
        #tabela.setModel(model)
        #tabela.resize(640, 480)
        #tabela.show()
        """# polaczenie = self.polaczenieBazy()
        sw = self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()
        sw.resize(640, 480)
        tabela = self.tableView
        tabela.horizontalHeader().setStretchLastSection(True)
        tabela.setWordWrap(True)
        tabela.setTextElideMode(QtCore.Qt.ElideLeft)
        tabela.setItemDelegateForColumn()
        model = QtSql.QSqlQueryModel()
        model.setQuery("SELECT * FROM Pracownicy")

        # dane = database.wyswietlPracownikow()

        # self.stworz_menu.addAction()"""


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = GlowneOkno()
    widget.show()

    app.exec_()
