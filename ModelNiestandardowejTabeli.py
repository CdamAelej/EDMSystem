import sys
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor

class ModelNiestandardowejTabeli(QAbstractTableModel):
    def __init__(self, dane = None):
        super(ModelNiestandardowejTabeli, self).__init__()
        self.zaladuj_dane(dane)

    def zaladuj_dane(self, dane):
        self.wprowadz_kolumny = dane[0].values
        self.wprowadz_wiersze = dane[1].values

        self.liczba_kolumn = 2
        self.liczba_wierszy = len(self.wprowadz_wiersze)

    def liczbaWierszy(self, parent = QModelIndex()):
        return self.liczba_wierszy

    def liczbaKolumn(self, parent = QModelIndex()):
        return self.liczba_kolumn

    def nazwyKolumn(self, ):
