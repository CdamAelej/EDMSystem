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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = GlowneOkno()
    widget.show()

    app.exec_()
