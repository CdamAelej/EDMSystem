from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class RysujDokument(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setAttribute(Qt.WA_StaticContents)
        w = 400
        h = 400
        self.szerokoscPisaka = 5
        self.kolorPisaka = Qt.black
        self.dokument = QImage(w, h, QImage.Format_RGB32)
        self.sciezka = QPainterPath()
        self.wyczyscDokument()

    def ustawKolorPisaka(self, nowyKolor):
        self.kolorPisaka = nowyKolor

    def ustawSzerokoscPisaka(self, nowaSzerokosc):
        self.szerokoscPisaka = nowaSzerokosc

    def wyczyscDokument(self):
        self.sciezka = QPainterPath()
        self.dokument.fill(Qt.white)
        self.update()

    def zapiszDokument(self, nazwaPliku, formatPliku):
        self.dokument.save(nazwaPliku, formatPliku)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.dokument, self.rect())

    def mousePressEventeEvent(self, event):
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

    zapisz_button.clicked.connect(lambda: tworz_dokument.zapiszObraz("dokument.png", "PNG"))
    wyczysc_button.clicked.connect(lambda: tworz_dokument.wyczyscDokument())

    widget.show()
    sys.exit(app.exec_())
