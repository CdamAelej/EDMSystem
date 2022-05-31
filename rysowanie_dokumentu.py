from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import datetime


class RysujDokument(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        """
        WA_StaticContents - Wskazuje, że zawartość widżetu jest wyrównana w kierunku północno-zachodnim i statyczna.
        Przy zmianie rozmiaru taki widżet otrzyma zdarzenia malowania tylko dla jego części, które są nowo widoczne.
        Ta flaga jest ustawiana lub usuwana przez autora widżetu.
        """
        self.setAttribute(Qt.WA_StaticContents)
        w = 400
        h = 400
        self.szerokoscPisaka = 5
        self.kolorPisaka = Qt.black
        # Ustawiam obszar rysowania
        self.dokument = QImage(w, h, QImage.Format_RGB32)
        # Ustawiam sciezke rysowania (szlaczek)
        self.sciezka = QPainterPath()
        self.wyczyscDokument()


    def wyczyscDokument(self):
        self.sciezka = QPainterPath()
        self.dokument.fill(Qt.white)
        self.update()

    def zapiszDokument(self, nazwaPliku, formatPliku):
        # dzisiaj = datetime.datetime.now()
        # data_czas = dzisiaj.strftime('%m/%d/%Y/%H:%M:%S')
        self.dokument.save(nazwaPliku, formatPliku)
        # print(str(data_czas))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.dokument, self.rect())

    def mousePressEvent(self, event):
        self.sciezka.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.sciezka.lineTo(event.pos())
        p = QPainter(self.dokument)
        p.setPen(QPen(self.kolorPisaka,
                      self.szerokoscPisaka, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        p.drawPath(self.sciezka)
        p.end()
        self.update()

    def sizeHint(self):
        return QSize(300, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    zapisz_button = QPushButton("Zapisz dokument")
    wyczysc_button = QPushButton("Wyczysc")
    tworz_dokument = RysujDokument()

    widget.setLayout(QVBoxLayout())
    widget.layout().addWidget(zapisz_button)
    widget.layout().addWidget(wyczysc_button)
    widget.layout().addWidget(tworz_dokument)

    zapisz_button.clicked.connect(lambda: tworz_dokument.zapiszDokument("dokument.png", "PNG"))
    wyczysc_button.clicked.connect(lambda: tworz_dokument.wyczyscDokument())

    widget.show()
    sys.exit(app.exec_())
