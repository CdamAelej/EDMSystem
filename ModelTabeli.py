from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class ModelTabeli(QtCore.QAbstractTableModel):
    def __init__(self, dane):
        super(ModelTabeli, self).__init__()
        self.dane = dane

    def dane(self, indeks, rola):
        if rola == Qt.DisplayRole:
            return self._dane[indeks.row()][indeks.column()]

    def liczbaWierszy(self, indeks):
        return len(self._dane)

    def liczbaKolumn(self, indeks):
        return len(self._dane[0])