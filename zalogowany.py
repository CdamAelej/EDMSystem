from database import Pracownik

class Zalogowany:
    def __init__(self, IDpracownika, Imie, Nazwisko, DataUrodzenia, su):
        self.IDpracownika = IDpracownika
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.DataUrodzenia = DataUrodzenia
        self.su = su
