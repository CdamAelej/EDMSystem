import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RysujDokument(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        h = 400
        w = 400
        self.szerokoscPisaka = 13
        self.kolorPisaka = Qt.black
        self.dokument = QImage(w, h, QImage.Format_RGB32)
        self.sciezka = QPainterPath()
        self.wyczyscDokument()

    def setPenColor(self, nowyKolor):
        self.kolorPisaka = nowyKolor

    def setPenWidth(self, nowaSzerokosc):
        self.szerokoscPisaka = nowaSzerokosc

    def wyczyscDokument(self):
        self.sciezka = QPainterPath()
        self.dokument.fill(Qt.white)  ## switch it to else
        self.update()

    def saveDokument(self, plikNazwa, plikFormat):
        self.dokument.save(plikNazwa, plikFormat)

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


def otworzMalarza():
    app = QApplication(sys.argv)
    w = QWidget()
    btnSave = QPushButton("Save dokument")
    btnClear = QPushButton("Clear")
    RysujDokument = RysujDokument()

    w.setLayout(QVBoxLayout())
    w.layout().addWidget(btnSave)
    w.layout().addWidget(btnClear)
    w.layout().addWidget(RysujDokument)

    btnSave.clicked.connect(lambda: RysujDokument.savedokument("dokument.png", "PNG"))
    btnClear.clicked.connect(RysujDokument.wyczyscDokument)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    otworzMalarza()