# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\program_diplom\designs\is_authenticated.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(689, 134)
        self.labelKey = QtWidgets.QLabel(Form)
        self.labelKey.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.labelKey.setObjectName("labelKey")
        self.textKey = QtWidgets.QLabel(Form)
        self.textKey.setGeometry(QtCore.QRect(10, 30, 671, 41))
        self.textKey.setText("")
        self.textKey.setWordWrap(True)
        self.textKey.setObjectName("textKey")
        self.textIsAuthenticated = QtWidgets.QLabel(Form)
        self.textIsAuthenticated.setGeometry(QtCore.QRect(10, 90, 671, 20))
        self.textIsAuthenticated.setText("")
        self.textIsAuthenticated.setAlignment(QtCore.Qt.AlignCenter)
        self.textIsAuthenticated.setObjectName("textIsAuthenticated")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelKey.setText(_translate("Form", "Восстановленный ключ:"))

