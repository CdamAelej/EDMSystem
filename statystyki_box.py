# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statystyki_box.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statystyki_form(object):
    def setupUi(self, statystyki_form):
        statystyki_form.setObjectName("statystyki_form")
        statystyki_form.resize(329, 200)
        self.formLayout = QtWidgets.QFormLayout(statystyki_form)
        self.formLayout.setObjectName("formLayout")
        self.statystykiSesji_label = QtWidgets.QLabel(statystyki_form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.statystykiSesji_label.setFont(font)
        self.statystykiSesji_label.setAlignment(QtCore.Qt.AlignCenter)
        self.statystykiSesji_label.setObjectName("statystykiSesji_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.statystykiSesji_label)
        self.ID_label = QtWidgets.QLabel(statystyki_form)
        self.ID_label.setObjectName("ID_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ID_label)
        self.IDtext_label = QtWidgets.QLabel(statystyki_form)
        self.IDtext_label.setObjectName("IDtext_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.IDtext_label)
        self.imieNazwisko_label = QtWidgets.QLabel(statystyki_form)
        self.imieNazwisko_label.setObjectName("imieNazwisko_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.imieNazwisko_label)
        self.imieNazwiskoText_label = QtWidgets.QLabel(statystyki_form)
        self.imieNazwiskoText_label.setObjectName("imieNazwiskoText_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.imieNazwiskoText_label)
        self.data_label = QtWidgets.QLabel(statystyki_form)
        self.data_label.setObjectName("data_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.data_label)
        self.dataText_label = QtWidgets.QLabel(statystyki_form)
        self.dataText_label.setObjectName("dataText_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dataText_label)
        self.su_label = QtWidgets.QLabel(statystyki_form)
        self.su_label.setObjectName("su_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.su_label)
        self.suText_label = QtWidgets.QLabel(statystyki_form)
        self.suText_label.setObjectName("suText_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.suText_label)
        self.liczbaDokumentow_label = QtWidgets.QLabel(statystyki_form)
        self.liczbaDokumentow_label.setObjectName("liczbaDokumentow_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.liczbaDokumentow_label)
        self.liczbaDokumentowText_label = QtWidgets.QLabel(statystyki_form)
        self.liczbaDokumentowText_label.setObjectName("liczbaDokumentowText_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.liczbaDokumentowText_label)
        self.liczbaPracownikow_label = QtWidgets.QLabel(statystyki_form)
        self.liczbaPracownikow_label.setObjectName("liczbaPracownikow_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.liczbaPracownikow_label)
        self.liczbaPracownikowText_label = QtWidgets.QLabel(statystyki_form)
        self.liczbaPracownikowText_label.setObjectName("liczbaPracownikowText_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.liczbaPracownikowText_label)

        self.retranslateUi(statystyki_form)
        QtCore.QMetaObject.connectSlotsByName(statystyki_form)

    def retranslateUi(self, statystyki_form):
        _translate = QtCore.QCoreApplication.translate
        statystyki_form.setWindowTitle(_translate("statystyki_form", "Statystyki sesji"))
        self.statystykiSesji_label.setText(_translate("statystyki_form", "Statystyki sesji"))
        self.ID_label.setText(_translate("statystyki_form", "ID zalogowanego pracownika: "))
        self.IDtext_label.setText(_translate("statystyki_form", "TextLabel"))
        self.imieNazwisko_label.setText(_translate("statystyki_form", "Imie i nazwisko zalogowanego pracownika:"))
        self.imieNazwiskoText_label.setText(_translate("statystyki_form", "TextLabel"))
        self.data_label.setText(_translate("statystyki_form", "Data urodzenia zalogowanego pracownika"))
        self.dataText_label.setText(_translate("statystyki_form", "TextLabel"))
        self.su_label.setText(_translate("statystyki_form", "Uprawnienia SU?"))
        self.suText_label.setText(_translate("statystyki_form", "TextLabel"))
        self.liczbaDokumentow_label.setText(_translate("statystyki_form", "Liczba dokumentow w systemie:"))
        self.liczbaDokumentowText_label.setText(_translate("statystyki_form", "TextLabel"))
        self.liczbaPracownikow_label.setText(_translate("statystyki_form", "Liczba pracownikow w systemie:"))
        self.liczbaPracownikowText_label.setText(_translate("statystyki_form", "TextLabel"))
