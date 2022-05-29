import os.path
import sys
import database
import sqlalchemy
from edms_box import Ui_ECDS_form
from PyQt5 import QtWidgets, QtCore
import sqlalchemy as db
from sqlalchemy.orm import *


# class BDelegat(QtWidgets.QStyledItemDelegate):


class GlowneOkno(QtWidgets.QMainWindow, Ui_ECDS_form):
    def __init__(self):
        super(GlowneOkno, self).__init__()
        self.setupUi(self)
        self.pokazPracownikow_action.triggered.connect(lambda: self.zaladujPracownikow())
        self.pokazDokumenty_action.triggered.connect(lambda: self.zaladujDokumenty())
        self.pokazDaneLogowania_action.triggered.connect(lambda: self.zaladujDaneLogowania())
        self.dodajPracownika_action.triggered.connect(lambda: self.dodajPracownika())


    """
    Tworze podokno w MDI Area o wielkosci 640x480, nastepnie tworze polaczenie z baza danych
    oraz tworze sesje, wczytuje tabele i wybieram wszystko z tabeli pracownicy po czym
    wyswietlam wiersze w tableWidget
    """
    def zaladujPracownikow(self,):
        sw = self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()
        sw.resize(640, 480)
        silnik = db.create_engine('sqlite:///bazafirmy.sqlite')
        polaczenie = silnik.connect()
        metadane = db.MetaData()
        pracownicy = db.Table('pracownicy', metadane, autoload=True, autoload_with=silnik)
        kolejka = db.select([pracownicy])
        wynikiPomocnik = polaczenie.execute(kolejka)
        wynikiZestaw = wynikiPomocnik.fetchall()
        self.tableWidget.setRowCount(2)
        tabelawiersze = 0
        for wiersz in wynikiZestaw:
            print(wiersz[0])
            self.tableWidget.setItem(tabelawiersze, 0, QtWidgets.QTableWidgetItem(str(wiersz[0])))
            self.tableWidget.setItem(tabelawiersze, 1, QtWidgets.QTableWidgetItem(str(wiersz[1])))
            self.tableWidget.setItem(tabelawiersze, 2, QtWidgets.QTableWidgetItem(str(wiersz[2])))
            self.tableWidget.setItem(tabelawiersze, 3, QtWidgets.QTableWidgetItem(str(wiersz[3])))
            self.tableWidget.setItem(tabelawiersze, 4, QtWidgets.QTableWidgetItem(str(wiersz[4])))
            tabelawiersze+=1

    def zaladujDokumenty(self,):
        sw = self.mdiArea.addSubWindow(self.pokazDokumenty_subwindow)
        self.pokazDokumenty_subwindow.show()
        sw.resize(640, 480)
        silnik = db.create_engine('sqlite:///bazafirmy.sqlite')
        polaczenie = silnik.connect()
        metadane = db.MetaData()
        dokumenty = db.Table('Dokumenty', metadane, autoload=True, autoload_with=silnik)
        kolejka = db.select([dokumenty])
        wynikiPomocnik = polaczenie.execute(kolejka)
        wynikiZestaw = wynikiPomocnik.fetchall()
        self.pokazDokumenty_tablewidget.setRowCount(2)
        tabelawiersze = 0
        for wiersz in wynikiZestaw:
            print(wiersz)
            self.pokazDokumenty_tablewidget.setItem(tabelawiersze, 0, QtWidgets.QTableWidgetItem(str(wiersz[0])))
            self.pokazDokumenty_tablewidget.setItem(tabelawiersze, 1, QtWidgets.QTableWidgetItem(str(wiersz[1])))
            self.pokazDokumenty_tablewidget.setItem(tabelawiersze, 2, QtWidgets.QTableWidgetItem(wiersz[2]))
            tabelawiersze += 1

    def zaladujDaneLogowania(self, ):
        sw = self.mdiArea.addSubWindow(self.pokazDaneLogowania_subwindow)
        self.pokazDaneLogowania_subwindow.show()
        sw.resize(640, 480)
        silnik = db.create_engine('sqlite:///bazafirmy.sqlite')
        polaczenie = silnik.connect()
        metadane = db.MetaData()
        daneLogowania = db.Table('DaneLogowania', metadane, autoload=True, autoload_with=silnik)
        kolejka = db.select([daneLogowania])
        wynikiPomocnik = polaczenie.execute(kolejka)
        wynikiZestaw = wynikiPomocnik.fetchall()
        self.pokazDaneLogowania_tableWidget.setRowCount(2)
        tabelawiersze = 0
        for wiersz in wynikiZestaw:
            print(wiersz)
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 0, QtWidgets.QTableWidgetItem(str(wiersz[0])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 1, QtWidgets.QTableWidgetItem(str(wiersz[1])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 2, QtWidgets.QTableWidgetItem(str(wiersz[2])))
            tabelawiersze += 1

    def dodajPracownika(self, ):
        sw = self.mdiArea.addSubWindow(self.dodajPracownika_subwindow)
        self.dodajPracownika_subwindow.show()
        if self.buttonBox.clicked(QtWidgets.QDialogButtonBox.Ok):
            imiePracownika = self.imiePracownika_lineEdit.text()
            nazwiskoPracownika = self.nazwiskoPracownika_lineEdit.text()
            dataUrodzenia = self.dataUrodzenia_dateEdit.date()
            login = self.loginPracownika_lineEdit
            haslo = self.hasloPracownika_lineEdit
            if self.uprawnieniaSU_checkBox.clicked():
                uprawnienia = True
            else:
                uprawnienia = False
            nowyPracownik = database.Pracownik(imie=imiePracownika, nazwisko=nazwiskoPracownika,
                                               dataUrodzenia=dataUrodzenia, su=uprawnienia)
            noweDaneLogowania = database.DaneLogowania(pracownik=nowyPracownik, login=login, haslo=haslo)
            with database.Session() as session:
                session.add(nowyPracownik)
                session.add(noweDaneLogowania)
                session.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = GlowneOkno()
    widget.show()

    app.exec_()
