from edms_box import Ui_ECDS_form
from PyQt5 import QtWidgets, QtCore
import sys


class GlowneOkno(QtWidgets.QMainWindow, Ui_ECDS_form):
    def __init__(self):
        super(GlowneOkno, self).__init__()
        self.setupUi(self)
        self.pokazPracownikow_action.triggered.connect(lambda: self.klikniecie())

    def klikniecie(self):
        sw = self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()
        sw.resize(640, 480)
        #self.stworz_menu.addAction()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = GlowneOkno()
    widget.show()

    app.exec_()
