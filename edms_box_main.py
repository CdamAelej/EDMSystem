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
        self.pokazDaneLogowania_subwindow.setWindowTitle("Dane Logowania")
        self.pokazDokumenty_subwindow.setWindowTitle("Dokumenty")
        self.subwindow.setWindowTitle("Pracownicy")
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
        self.otworzOkno_action.triggered.connect(lambda: self.brakModulu())
        self.pokazTabele_action.triggered.connect(lambda: self.brakModulu())
        self.usunPracownika_action.triggered.connect(lambda: self.brakModulu())

    """
    Funkcja odpowiadajaca za pojawienie sie informacji o nieistniejacym module
    """
    def brakModulu(self, ):
        QMessageBox.information(self, "Brak modulu", "Modul nie istnieje. Upewnij sie ze wszystkie pliki zopstaly poprawnie pobrane")

    """
    Funkcja odpowiadająca za otworzenie okna w ktorym moge odrecznie stworzyc dokument
    Niestety funkcja nie dziala poprawnie i zalecam po prostu uruchomienie rysowanie_dokumentu.py
    """
    def rysujDokument(self, ):
        #bom = QApplication(sys.argv)
        wi = QWidget()
        zapisz_button = QPushButton("Zapisz dokument")
        wyczysc_button = QPushButton("Wyczysc")
        tworz_dokument = RysujDokument()

        widget.setLayout(QVBoxLayout())
        widget.layout().addWidget(zapisz_button)
        widget.layout().addWidget(wyczysc_button)
        widget.layout().addWidget(tworz_dokument)

        zapisz_button.clicked.connect(lambda: tworz_dokument.zapiszObraz("dokument.png", "PNG"))
        wyczysc_button.clicked.connect(lambda: tworz_dokument.wyczyscDokument())

        wi.show()


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
        silnik = db.create_engine('sqlite:///databases/bazafirmy.sqlite')
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

    """
    Dziala na tej samej zasadzie co zaladujPracownikow() tylko operujemy na tabeli Dokumenty
    """
    def zaladujDokumenty(self,):
        sw = self.mdiArea.addSubWindow(self.pokazDokumenty_subwindow)
        self.pokazDokumenty_subwindow.show()
        sw.resize(640, 480)
        silnik = db.create_engine('sqlite:///databases/bazafirmy.sqlite')
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

    """
    Dziala na tej samej zasadzie co zaladujPracownikow() tylko operujemy na tabeli DaneLogowania
    """
    def zaladujDaneLogowania(self, ):
        sw = self.mdiArea.addSubWindow(self.pokazDaneLogowania_subwindow)
        self.pokazDaneLogowania_subwindow.show()
        sw.resize(640, 480)
        silnik = db.create_engine('sqlite:///databases/bazafirmy.sqlite')
        polaczenie = silnik.connect()
        metadane = db.MetaData()
        daneLogowania = db.Table('DaneLogowania', metadane, autoload=True, autoload_with=silnik)
        kolejka = db.select([daneLogowania])
        wynikiPomocnik = polaczenie.execute(kolejka)
        wynikiZestaw = wynikiPomocnik.fetchall()
        liczbawierszy = 2
        self.pokazDaneLogowania_tableWidget.setRowCount(liczbawierszy)
        tabelawiersze = 0
        for wiersz in wynikiZestaw:
            print(wiersz)
            self.pokazDaneLogowania_tableWidget.setRowCount(liczbawierszy)
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 0, QTableWidgetItem(str(wiersz[0])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 1, QTableWidgetItem(str(wiersz[1])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 2, QTableWidgetItem(str(wiersz[2])))
            self.pokazDaneLogowania_tableWidget.setItem(tabelawiersze, 3, QTableWidgetItem(str(wiersz[3])))
            tabelawiersze += 1
            liczbawierszy+=1

    """
    Wczytuje dane z labelek w podoknie dodajPracownika_subwindow, tworze nowe obiekty klas Pracownik()
    oraz DaneLogowania, tworze polaczenie z baza danych oraz wstawiam obiekty do odpowiednich tabel
    """
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

    """
    Otwieram podokno dodajPracownika_subwindow, wylaczam usuwanie okna przy zamykaniu i na klikniecie 
    buttonBoxa wywoluje funkcje wstawPracownika()
    """
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
