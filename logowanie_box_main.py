from logowanie_box import Ui_Logowanie
from edms_box_main import GlowneOkno
from PyQt5 import QtWidgets
import database as db
import sqlite3
from zalogowany import Zalogowany
from statystyki_box_main import zalogowanyUzytkownik
dbconnect = sqlite3.connect('bazafirmy.sqlite')


class OknoLogowania(QtWidgets.QWidget, Ui_Logowanie):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Logowanie")
        self.zatwierdz_button.clicked.connect(self.autoryzacja)


    """
    Funkcja odpowiadajaca za autoryzacje logowania
    Pobieram login i haslo z labelek, w tabeli DaneLogowania sprawdzam czy istnieje takie konto
    Jesli istnieje to tworze zalogowanego uzytkownika do statystyk , pokazuje okno z informacja
    O pomyslnym zalogowaniu, zamykam okno logowania i otwieram glowne okno aplikacji
    Jesli logowanie jest niepoprawne wyswietlam o tym informacje i pozwalam uzytkownikowi na nastepna
    Probe zalogowania
    """
    def autoryzacja(self):
        Login = self.login_edit.text()
        haslo = self.haslo_edit.text()
        wiersz = db.session.query(db.DaneLogowania).filter(db.DaneLogowania.login == Login, db.DaneLogowania.haslo == haslo).first()
        if wiersz:
            kolejka = db.session.query(db.Pracownik).filter(db.Pracownik.id_pracownika == wiersz.id_pracownika).first()
            zalogowanyUzytkownik_pomocnik = Zalogowany(kolejka.id_pracownika, kolejka.imie, kolejka.nazwisko, kolejka.data_urodzenia, kolejka.su)
            zalogowanyUzytkownik = zalogowanyUzytkownik_pomocnik
            print(zalogowanyUzytkownik.IDpracownika, zalogowanyUzytkownik.Imie, zalogowanyUzytkownik.Nazwisko, zalogowanyUzytkownik.DataUrodzenia, zalogowanyUzytkownik.su)
            self.close()
            QtWidgets.QMessageBox.information(self, 'Zalogowano', 'Pomyślnie zalogowano')
            widget = GlowneOkno()
            widget.show()
        else:
            self.close()
            QtWidgets.QMessageBox.information(self, 'Błąd', 'Podałeś błędny login lub hasło ')
            self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = OknoLogowania()
    widget.show()

    app.exec_()
