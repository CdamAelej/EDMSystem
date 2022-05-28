import os.path
import sys
from edms_box import Ui_ECDS_form
from PyQt5 import QtWidgets, QtCore, QtSql



#class BDelegat(QtWidgets.QStyledItemDelegate):


class GlowneOkno(QtWidgets.QMainWindow, Ui_ECDS_form):
    def __init__(self):
        super(GlowneOkno, self).__init__()
        self.setupUi(self)
        self.pokazPracownikow_action.triggered.connect(lambda: self.zaladujPracownikow())

    def polaczenieBazy(self):
        bazaDanych = QtSql.QSqlDatabase("bazafirmy")
        plik = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bazafirmy.sqlite")
        bazaDanych.setDatabaseName(plik)
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
        return True

    def zaladujPracownikow(self, str):
        #polaczenie = self.polaczenieBazy()
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

        #dane = database.wyswietlPracownikow()

        #self.stworz_menu.addAction()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = GlowneOkno()
    widget.show()

    app.exec_()
