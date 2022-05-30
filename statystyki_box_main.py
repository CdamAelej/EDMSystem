from statystyki_box import Ui_statystyki_form
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtWidgets
from zalogowany import Zalogowany
import sys
import multiprocessing

class Statystyki(QWidget, Ui_statystyki_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.IDtext_label.setText(zalogowanyUzytkownik.IDpracownika)


#watek1 = multiprocessing.Process()
zalogowanyUzytkownik = None # Zalogowany(None, None, None, None, None)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Statystyki()
    widget.show()

    app.exec_()