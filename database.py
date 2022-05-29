from datetime import date
from sqlalchemy import *
from sqlalchemy.orm import *

# lacze z baza danych
engine = create_engine('sqlite:///bazafirmy.sqlite', echo=True)
Session = sessionmaker(engine)
# zarzadzamie tabelami
base = declarative_base()

"""
Tworze klase Pracownik ktora odpowiada za stworzenie tabeli Pracownicy
Dzieki jej konstruktorowi moge tworzyc nowe rekordy do tabel. Tak samo
dzialaja klasy DaneLogowania oraz Dokumenty. Klasy (tabele) DaneLogowania oraz
Dokumenty sa w relacji z Pracownikami
"""


class Pracownik(base):
    __tablename__ = 'Pracownicy'

    id_pracownika = Column(Integer, primary_key=True, name="IDpracownika")
    imie = Column(String(30), name="Imie")
    nazwisko = Column(String(30), name="Nazwisko")
    data_urodzenia = Column(Date, name="DataUrodzenia")
    su = Column(Boolean)
    dokumenty = relationship("Dokumenty", back_populates="pracownik")
    dane_logowania = relationship("DaneLogowania", back_populates="pracownik")


class DaneLogowania(base):
    __tablename__ = 'DaneLogowania'

    id_danych_logowania = Column(Integer, primary_key=True,
                                 name="IDDanychLogowania")
    id_pracownika = Column(Integer, ForeignKey("Pracownicy.IDpracownika"),
                           name="IDPracownika")
    pracownik = relationship("Pracownik", back_populates="dane_logowania")
    login = Column(String(255), name="Login")
    haslo = Column(String(255), name="Haslo")


class Dokumenty(base):
    __tablename__ = 'Dokumenty'

    id_dokumentu = Column(Integer, primary_key=True, name="IDdokumentu")
    id_pracownika = Column(Integer, ForeignKey('Pracownicy.IDpracownika'),
                           name="IDpracownika")
    typ_dokumentu = Column(String(3), name="TypDokumentu")
    pracownik = relationship("Pracownik", back_populates="dokumenty")


base.metadata.create_all(engine)

# Tworze listy w ktorych tworze nowe rekordy do tabel Pracownicy oraz DaneLogowania
pracownicy_do_dodania = [
    Pracownik(imie="Adam", nazwisko="Celej",
              data_urodzenia=date(2001, 5, 10), su=True),
    Pracownik(imie="Marek", nazwisko="Kowalski",
              data_urodzenia=date(1986, 12, 10), su=False)
]

dane_logowania_do_dodania = [
    DaneLogowania(pracownik=pracownicy_do_dodania[0], login="adamcelej",
                  haslo="brakmuzgu"),
    DaneLogowania(pracownik=pracownicy_do_dodania[1], login="marekkowalski",
                  haslo="wiemwszystko")
]

# Tworze sesje oraz wstawiam powyzsze rekordy do bazy
with Session() as session:
    if session is null:
        session.add_all(pracownicy_do_dodania)
        session.add_all(dane_logowania_do_dodania)
        session.commit()


def wyswietlPracownikow():
    selekcja = select(Pracownik)
    wyniki = engine.connect().execute(selekcja)
    for wiersz in wyniki:
        print(wiersz)

# wyswietlPracownikow()
