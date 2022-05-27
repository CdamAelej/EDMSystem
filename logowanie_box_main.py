from logowanie_box import Ui_Logowanie
from PyQt5 import QtWidgets, QtCore
import sqlite3

dbconnect = sqlite3.connect('bazafirmy.sqlite')

class OknoLogowania(QtWidgets.QWidget, Ui_Logowanie):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.zatwierdz_button.clicked.connect(self.autoryzacja)

    def autoryzacja(self):
        Login = self.login_edit.text()
        haslo = self.haslo_edit.text()


        if Login == 'adamcelej' and haslo == 'brakmuzgu':
            self.close()
            QtWidgets.QMessageBox.information(self, 'Zalogowano', 'Pomyślnie zalogowano')
        else:
            self.close()
            QtWidgets.QMessageBox.information(self, 'Błąd', 'Podałeś błędny login lub hasło ')
            self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = OknoLogowania()
    widget.show()

    app.exec_()