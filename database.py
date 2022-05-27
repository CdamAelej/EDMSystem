from sqlalchemy import *
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import *

#łączę z bazą danych
engine = create_engine('sqlite:///bazafirmy.sqlite', echo=True)
#zarzadzamie tabelami
base = declarative_base()


class Pracownicy(base):

    __tablename__ = 'Pracownicy'

    IDpracownika = Column(Integer, primary_key=True)
    Imie = Column(String(30))
    Nazwisko = Column(String(30))
    DataUrodzenia = Column(Date)
    su = Column(Boolean)


    def __init__(self, IDpracownika, Imie, Nazwisko, DataUrodzenia, su):
        self.IDpracownika = IDpracownika
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.DataUrodzenia = DataUrodzenia
        self.su = su

class DaneLogowania(base):

    __tablename__ = 'DaneLogowania'

    IDpracownika = Column(Integer, primary_key=True)
    login = Column(String(255))
    haslo = Column(String(255))

    def __init__(self, IDpracownika, login, haslo):
        self.IDpracownika = IDpracownika
        self.login = login
        self.haslo = haslo

class Dokumenty(base):

    __tablename__ = 'Dokumenty'

    IDdokumentu = Column(Integer, primary_key=True)
    IDpracownika = Column(Integer)
    TypDokumentu = Column(String(3))

    def __init__(self, IDdokumentu, IDpracownika, TypDokumentu):
        self.IDdokumentu = IDdokumentu
        self.IDpracownika = IDpracownika
        self.TypDokumentu = TypDokumentu

base.metadata.create_all(engine)

Pracownicy.insert().values([
    {"IDpracownika": "0"},
    {"Imie": "Adam"},
    {"Nazwisko": "Celej"},
    {"DataUrodzenia": "20010510"},
    {"su": "True"}
])

DaneLogowania.insert().values([
    {"IDpracownika": "0"},
    {"login": "adamcelej"},
    {"haslo": "brakmuzgu"}
])