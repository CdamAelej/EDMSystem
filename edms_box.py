# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edms_box.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ECDS_form(object):
    def setupUi(self, ECDS_form):
        ECDS_form.setObjectName("ECDS_form")
        ECDS_form.resize(1727, 821)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ECDS_form.sizePolicy().hasHeightForWidth())
        ECDS_form.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ECDS_form)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setEnabled(True)
        self.mdiArea.setObjectName("mdiArea")
        self.subwindow = QtWidgets.QWidget()
        self.subwindow.setEnabled(False)
        self.subwindow.setObjectName("subwindow")
        self.tableWidget = QtWidgets.QTableWidget(self.subwindow)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QtCore.QRect(-4, 0, 551, 331))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pokazDokumenty_subwindow = QtWidgets.QWidget()
        self.pokazDokumenty_subwindow.setObjectName("pokazDokumenty_subwindow")
        self.pokazDokumenty_tablewidget = QtWidgets.QTableWidget(self.pokazDokumenty_subwindow)
        self.pokazDokumenty_tablewidget.setEnabled(False)
        self.pokazDokumenty_tablewidget.setGeometry(QtCore.QRect(5, 1, 551, 321))
        self.pokazDokumenty_tablewidget.setRowCount(2)
        self.pokazDokumenty_tablewidget.setObjectName("pokazDokumenty_tablewidget")
        self.pokazDokumenty_tablewidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.pokazDokumenty_tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pokazDokumenty_tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pokazDokumenty_tablewidget.setHorizontalHeaderItem(2, item)
        self.pokazDaneLogowania_subwindow = QtWidgets.QWidget()
        self.pokazDaneLogowania_subwindow.setObjectName("pokazDaneLogowania_subwindow")
        self.pokazDaneLogowania_tableWidget = QtWidgets.QTableWidget(self.pokazDaneLogowania_subwindow)
        self.pokazDaneLogowania_tableWidget.setEnabled(False)
        self.pokazDaneLogowania_tableWidget.setGeometry(QtCore.QRect(10, 10, 321, 91))
        self.pokazDaneLogowania_tableWidget.setRowCount(2)
        self.pokazDaneLogowania_tableWidget.setColumnCount(3)
        self.pokazDaneLogowania_tableWidget.setObjectName("pokazDaneLogowania_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.pokazDaneLogowania_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pokazDaneLogowania_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pokazDaneLogowania_tableWidget.setHorizontalHeaderItem(2, item)
        self.dodajPracownika_subwindow = QtWidgets.QWidget()
        self.dodajPracownika_subwindow.setObjectName("dodajPracownika_subwindow")
        self.formLayout_2 = QtWidgets.QFormLayout(self.dodajPracownika_subwindow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.dodajPracownika_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dodajPracownika_label.setFont(font)
        self.dodajPracownika_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dodajPracownika_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dodajPracownika_label.setObjectName("dodajPracownika_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.dodajPracownika_label)
        self.imiePracownika_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        self.imiePracownika_label.setObjectName("imiePracownika_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.imiePracownika_label)
        self.imiePracownika_lineEdit = QtWidgets.QLineEdit(self.dodajPracownika_subwindow)
        self.imiePracownika_lineEdit.setObjectName("imiePracownika_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.imiePracownika_lineEdit)
        self.nazwiskoPracownika_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        self.nazwiskoPracownika_label.setObjectName("nazwiskoPracownika_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nazwiskoPracownika_label)
        self.nazwiskoPracownika_lineEdit = QtWidgets.QLineEdit(self.dodajPracownika_subwindow)
        self.nazwiskoPracownika_lineEdit.setObjectName("nazwiskoPracownika_lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nazwiskoPracownika_lineEdit)
        self.dataUrodzenia_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        self.dataUrodzenia_label.setObjectName("dataUrodzenia_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dataUrodzenia_label)
        self.loginPracownika_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        self.loginPracownika_label.setObjectName("loginPracownika_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.loginPracownika_label)
        self.loginPracownika_lineEdit = QtWidgets.QLineEdit(self.dodajPracownika_subwindow)
        self.loginPracownika_lineEdit.setObjectName("loginPracownika_lineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.loginPracownika_lineEdit)
        self.hasloPracownik_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        self.hasloPracownik_label.setObjectName("hasloPracownik_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.hasloPracownik_label)
        self.hasloPracownika_lineEdit = QtWidgets.QLineEdit(self.dodajPracownika_subwindow)
        self.hasloPracownika_lineEdit.setObjectName("hasloPracownika_lineEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.hasloPracownika_lineEdit)
        self.uprawnieniaSU_label = QtWidgets.QLabel(self.dodajPracownika_subwindow)
        self.uprawnieniaSU_label.setObjectName("uprawnieniaSU_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.uprawnieniaSU_label)
        self.uprawnieniaSU_checkBox = QtWidgets.QCheckBox(self.dodajPracownika_subwindow)
        self.uprawnieniaSU_checkBox.setObjectName("uprawnieniaSU_checkBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.uprawnieniaSU_checkBox)
        self.dataUrodzenia_dateEdit = QtWidgets.QDateEdit(self.dodajPracownika_subwindow)
        self.dataUrodzenia_dateEdit.setObjectName("dataUrodzenia_dateEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dataUrodzenia_dateEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.dodajPracownika_subwindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mdiArea)
        ECDS_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ECDS_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1727, 21))
        self.menubar.setObjectName("menubar")
        self.menuDokumenty = QtWidgets.QMenu(self.menubar)
        self.menuDokumenty.setObjectName("menuDokumenty")
        self.stworz_menu = QtWidgets.QMenu(self.menuDokumenty)
        self.stworz_menu.setObjectName("stworz_menu")
        self.menuStatystyka = QtWidgets.QMenu(self.menubar)
        self.menuStatystyka.setObjectName("menuStatystyka")
        self.menuBaza_danych = QtWidgets.QMenu(self.menubar)
        self.menuBaza_danych.setObjectName("menuBaza_danych")
        ECDS_form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ECDS_form)
        self.statusbar.setObjectName("statusbar")
        ECDS_form.setStatusBar(self.statusbar)
        self.otworz_action = QtWidgets.QAction(ECDS_form)
        self.otworz_action.setObjectName("otworz_action")
        self.otworzOkno_action = QtWidgets.QAction(ECDS_form)
        self.otworzOkno_action.setObjectName("otworzOkno_action")
        self.pokazPracownikow_action = QtWidgets.QAction(ECDS_form)
        self.pokazPracownikow_action.setVisible(True)
        self.pokazPracownikow_action.setObjectName("pokazPracownikow_action")
        self.wyslij_action = QtWidgets.QAction(ECDS_form)
        self.wyslij_action.setObjectName("wyslij_action")
        self.pokazDokumenty_action = QtWidgets.QAction(ECDS_form)
        self.pokazDokumenty_action.setObjectName("pokazDokumenty_action")
        self.dodajPracownika_action = QtWidgets.QAction(ECDS_form)
        self.dodajPracownika_action.setObjectName("dodajPracownika_action")
        self.pokazDaneLogowania_action = QtWidgets.QAction(ECDS_form)
        self.pokazDaneLogowania_action.setObjectName("pokazDaneLogowania_action")
        self.pokazTabele_action = QtWidgets.QAction(ECDS_form)
        self.pokazTabele_action.setObjectName("pokazTabele_action")
        self.usunPracownika_action = QtWidgets.QAction(ECDS_form)
        self.usunPracownika_action.setObjectName("usunPracownika_action")
        self.automatycznie_action = QtWidgets.QAction(ECDS_form)
        self.automatycznie_action.setObjectName("automatycznie_action")
        self.recznie_action = QtWidgets.QAction(ECDS_form)
        self.recznie_action.setObjectName("recznie_action")
        self.odrecznie_action = QtWidgets.QAction(ECDS_form)
        self.odrecznie_action.setObjectName("odrecznie_action")
        self.stworz_menu.addAction(self.automatycznie_action)
        self.stworz_menu.addAction(self.recznie_action)
        self.stworz_menu.addAction(self.odrecznie_action)
        self.menuDokumenty.addAction(self.stworz_menu.menuAction())
        self.menuDokumenty.addAction(self.otworz_action)
        self.menuDokumenty.addAction(self.wyslij_action)
        self.menuStatystyka.addAction(self.otworzOkno_action)
        self.menuBaza_danych.addAction(self.pokazPracownikow_action)
        self.menuBaza_danych.addAction(self.pokazDokumenty_action)
        self.menuBaza_danych.addSeparator()
        self.menuBaza_danych.addAction(self.dodajPracownika_action)
        self.menuBaza_danych.addAction(self.pokazDaneLogowania_action)
        self.menuBaza_danych.addAction(self.pokazTabele_action)
        self.menuBaza_danych.addAction(self.usunPracownika_action)
        self.menubar.addAction(self.menuDokumenty.menuAction())
        self.menubar.addAction(self.menuStatystyka.menuAction())
        self.menubar.addAction(self.menuBaza_danych.menuAction())

        self.retranslateUi(ECDS_form)
        QtCore.QMetaObject.connectSlotsByName(ECDS_form)

    def retranslateUi(self, ECDS_form):
        _translate = QtCore.QCoreApplication.translate
        ECDS_form.setWindowTitle(_translate("ECDS_form", "Electronic Documents Management System"))
        self.subwindow.setWindowTitle(_translate("ECDS_form", "Podokno"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ECDS_form", "IDpracownika"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ECDS_form", "Imie"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ECDS_form", "Nazwisko"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ECDS_form", "DataUrodzenia"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ECDS_form", "su"))
        self.pokazDokumenty_subwindow.setWindowTitle(_translate("ECDS_form", "Podokno"))
        item = self.pokazDokumenty_tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("ECDS_form", "IDdokumentu"))
        item = self.pokazDokumenty_tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("ECDS_form", "IDpracownika"))
        item = self.pokazDokumenty_tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("ECDS_form", "TypDokumentu"))
        self.pokazDaneLogowania_subwindow.setWindowTitle(_translate("ECDS_form", "Podokno"))
        item = self.pokazDaneLogowania_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ECDS_form", "IDpracownika"))
        item = self.pokazDaneLogowania_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ECDS_form", "Login"))
        item = self.pokazDaneLogowania_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ECDS_form", "Haslo"))
        self.dodajPracownika_subwindow.setWindowTitle(_translate("ECDS_form", "Podokno"))
        self.dodajPracownika_label.setText(_translate("ECDS_form", "Dodaj pracownika"))
        self.imiePracownika_label.setText(_translate("ECDS_form", "Podaj imie pracownika"))
        self.nazwiskoPracownika_label.setText(_translate("ECDS_form", "Podaj nazwisko pracownika"))
        self.dataUrodzenia_label.setText(_translate("ECDS_form", "Podaj date urodzenia pracownika"))
        self.loginPracownika_label.setText(_translate("ECDS_form", "Podaj nowy login dla pracownika"))
        self.hasloPracownik_label.setText(_translate("ECDS_form", "Podaj nowe haslo dla pracownika"))
        self.uprawnieniaSU_label.setText(_translate("ECDS_form", "Czy pracownik ma uprawnienia su?"))
        self.uprawnieniaSU_checkBox.setText(_translate("ECDS_form", "CheckBox"))
        self.menuDokumenty.setTitle(_translate("ECDS_form", "Dokumenty"))
        self.stworz_menu.setTitle(_translate("ECDS_form", "Stworz"))
        self.menuStatystyka.setTitle(_translate("ECDS_form", "Statystyka"))
        self.menuBaza_danych.setTitle(_translate("ECDS_form", "Baza danych"))
        self.otworz_action.setText(_translate("ECDS_form", "Otworz"))
        self.otworzOkno_action.setText(_translate("ECDS_form", "Otworz okno"))
        self.pokazPracownikow_action.setText(_translate("ECDS_form", "Pokaz pracownikow"))
        self.wyslij_action.setText(_translate("ECDS_form", "Wyslij"))
        self.pokazDokumenty_action.setText(_translate("ECDS_form", "Pokaż dokumenty"))
        self.dodajPracownika_action.setText(_translate("ECDS_form", "Dodaj pracownika"))
        self.pokazDaneLogowania_action.setText(_translate("ECDS_form", "Pokaz dane logowania"))
        self.pokazTabele_action.setText(_translate("ECDS_form", "Pokaz tabele"))
        self.usunPracownika_action.setText(_translate("ECDS_form", "Usun pracownika"))
        self.automatycznie_action.setText(_translate("ECDS_form", "Automatycznie"))
        self.recznie_action.setText(_translate("ECDS_form", "Recznie"))
        self.odrecznie_action.setText(_translate("ECDS_form", "Odrecznie"))
