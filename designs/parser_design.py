# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\program_diplom\parser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 361, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelStep = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelStep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStep.setObjectName("labelStep")
        self.gridLayout.addWidget(self.labelStep, 3, 0, 1, 1)
        self.textStep = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.textStep.setObjectName("textStep")
        self.gridLayout.addWidget(self.textStep, 3, 1, 1, 1)
        self.buttonBrowseDataFolder = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonBrowseDataFolder.setObjectName("buttonBrowseDataFolder")
        self.gridLayout.addWidget(self.buttonBrowseDataFolder, 2, 0, 1, 1)
        self.textBrowseDataFolder = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.textBrowseDataFolder.setObjectName("textBrowseDataFolder")
        self.gridLayout.addWidget(self.textBrowseDataFolder, 2, 1, 1, 1)
        self.labelProc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelProc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelProc.setObjectName("labelProc")
        self.gridLayout.addWidget(self.labelProc, 4, 0, 1, 1)
        self.textProc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.textProc.setObjectName("textProc")
        self.gridLayout.addWidget(self.textProc, 4, 1, 1, 1)
        self.buttonParseData = QtWidgets.QPushButton(Form)
        self.buttonParseData.setGeometry(QtCore.QRect(140, 230, 121, 23))
        self.buttonParseData.setObjectName("buttonParseData")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelStep.setText(_translate("Form", "Шаг выборки:"))
        self.buttonBrowseDataFolder.setText(_translate("Form", "Browse Data Folder"))
        self.labelProc.setText(_translate("Form", "Доля тестовых данных:"))
        self.buttonParseData.setText(_translate("Form", "Parse"))

