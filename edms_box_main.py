import datetime
import os.path
import sys
import database
import sqlalchemy

import rysowanie_dokumentu
from edms_box import Ui_ECDS_form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlalchemy as db
from sqlalchemy.orm import *
from statystyki_box_main import Statystyki
from rysowanie_dokumentu import RysujDokument


class GlowneOkno(QMainWindow, Ui_ECDS_form):
    def __init__(self):
        super(GlowneOkno, self).__init__()
        self.setupUi(self)
        self.dodajPracownika_subwindow.setWindowTitle("Dodaj pracownika")
        self.pokazPracownikow_action.triggered.connect(lambda: self.zaladujPracownikow())
        self.pokazDokumenty_action.triggered.connect(lambda: self.zaladujDokumenty())
        self.pokazDaneLogowania_action.triggered.connect(lambda: self.zaladujDaneLogowania())
        self.dodajPracownika_action.triggered.connect(lambda: self.dodajPracownika())
        self.automatycznie_action.triggered.connect(lambda: self.brakModulu())
        self.automatycznie_action.setVisible(False)
        self.recznie_action.triggered.connect(lambda: self.brakModulu())
        self.odrecznie_action.triggered.connect(lambda: self.rysujDokument())
        self.otworz_action.triggered.connect(lambda: self.brakModulu())
        self.wyslij_action.triggered.connect(lambda: self.brakModulu())
        self.otworzOkno_action.triggered.connect(lambda: self.pokazStatystyki())
        self.pokazTabele_action.triggered.connect(lambda: self.brakModulu())
        self.usunPracownika_action.triggered.connect(lambda: self.brakModulu())

    def brakModulu(self, ):
        QMessageBox.information(self, "Brak modulu", "Modul nie istnieje. Upewnij sie ze wszystkie pliki zopstaly poprawnie pobrane")

    def rysujDokument(self, ):
        widget = rysowanie_dokumentu.RysujDokument()
        widget.setVisible(True)



    def pokazStatystyki(self,):
        #aplikacja = QApplication(sys.argv)
        statystyki = Statystyki()
        statystyki.show()
        #aplikacja.exec_()


    """
    Tworze podokno w MDI Area o wielkosci 640x480, nastepnie tworze polaczenie z baza danych
    oraz tworze sesje, wczytuje tabele i wybieram wszystko z tabeli pracownicy po czym
    wyswietlam wiersze w tableWidget
    """
    def zaladujPracownikow(self,):
        sw = self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()
        self.tableWidget.setVisible(True)
        sw.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        sw.resize(640, 480)
        silnik = db.create_engine('sqlite:///bazafirmy.sqlite')
        polaczenie = silnik.connect()
        metadane = db.MetaData()
        pracownicy = db.Table('pracownicy', metadane, autoload=True, autoload_with=silnik)
        kolejka = db.select([pracownicy])
        wynikiPomocnik = polaczenie.execute(kolejka)
        wynikiZestaw = wynikiPomocnik.fetchall()
        liczbaWierszy = 2
        self.tableWidget.setRowCount(liczbaWierszy)
        tabelawiersze = 0
        for wiersz in wynikiZestaw:
            print(wiersz[0])
            liczbaWierszy+=1
            self.tableWidget.setRowCount(liczbaWierszy)
            self.tableWidget.setItem(tabelawiersze, 0, QTableWidgetItem(str(wiersz[0])))
            self.tableWidget.setItem(tabelawiersze, 1, QTableWidgetItem(str(wiersz[1])))
            self.tableWidget.setItem(tabelawiersze, 2, QTableWidgetItem(str(wiersz[2])))
            self.tableWidget.setItem(tabelawiersze, 3, QTableWidgetItem(str(wiersz[3])))
            self.tableWidget.setItem(tabelawiersze, 4, QTableWidgetItem(str(wiersz[4])))
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
            self.pokazDokumenty_tablewidget.setItem(tabelawiersze, 0, QTableWidgetItem(str(wiersz[0])))
            self.pokazDokumenty_tablewidget.setItem(tabelawiersze, 1, QTableWidgetItem(str(wiersz[1])))
            self.pokazDokumenty_tablewidget.setItem(tabelawiersze, 2, QTableWidgetItem(wiersz[2]))
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
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 0, QTableWidgetItem(str(wiersz[0])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 1, QTableWidgetItem(str(wiersz[1])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 2, QTableWidgetItem(str(wiersz[2])))
            tabelawiersze += 1

    def wstawPracownika(self, ):
        imiePracownika = self.imiePracownika_lineEdit.text()
        nazwiskoPracownika = self.nazwiskoPracownika_lineEdit.text()
        dataUrodzenia = self.dataUrodzenia_dateEdit.date() # self.dataUrodzenia_dateEdit.date()
        dataUrodzenia2= dataUrodzenia.toPyDate()
        login = self.loginPracownika_lineEdit.text()
        haslo = self.hasloPracownika_lineEdit.text()
        x = self.uprawnieniaSU_checkBox.isChecked()
        if x == True:
            uprawnienia = True
        else:
            uprawnienia = False
        nowyPracownik = database.Pracownik(imie=imiePracownika, nazwisko=nazwiskoPracownika,
                                           data_urodzenia=dataUrodzenia2, su=uprawnienia)
        noweDaneLogowania = database.DaneLogowania(pracownik=nowyPracownik, login=login, haslo=haslo)
        with database.Session() as session:
            session.add(nowyPracownik)
            session.add(noweDaneLogowania)
            session.commit()
        #self.dodajPracownika_subwindow.setVisible(False)
        QMessageBox.information(self, "Dodano pracownika", "Pracownik zostal poprawnie dodany do systemu")

    def dodajPracownika(self, ):
        podokno = self.mdiArea.addSubWindow(self.dodajPracownika_subwindow)
        podokno.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        self.dodajPracownika_subwindow.show()
        self.buttonBox.clicked.connect(lambda: self.wstawPracownika())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = GlowneOkno()
    widget.show()

    app.exec_()
