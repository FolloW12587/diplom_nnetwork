# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\program_diplom\designs\prog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelModel = QtWidgets.QLabel(self.centralwidget)
        self.labelModel.setGeometry(QtCore.QRect(20, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelModel.setFont(font)
        self.labelModel.setObjectName("labelModel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelData = QtWidgets.QLabel(self.centralwidget)
        self.labelData.setGeometry(QtCore.QRect(20, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelData.setFont(font)
        self.labelData.setObjectName("labelData")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 180, 191, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTrainCount = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelTrainCount.setObjectName("labelTrainCount")
        self.gridLayout.addWidget(self.labelTrainCount, 0, 0, 1, 1)
        self.labelTestCount = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelTestCount.setObjectName("labelTestCount")
        self.gridLayout.addWidget(self.labelTestCount, 1, 0, 1, 1)
        self.textTrainCount = QtWidgets.QLabel(self.gridLayoutWidget)
        self.textTrainCount.setObjectName("textTrainCount")
        self.gridLayout.addWidget(self.textTrainCount, 0, 1, 1, 1)
        self.textTestCount = QtWidgets.QLabel(self.gridLayoutWidget)
        self.textTestCount.setObjectName("textTestCount")
        self.gridLayout.addWidget(self.textTestCount, 1, 1, 1, 1)
        self.progressData = QtWidgets.QProgressBar(self.centralwidget)
        self.progressData.setGeometry(QtCore.QRect(387, 380, 391, 23))
        self.progressData.setProperty("value", 0)
        self.progressData.setTextVisible(False)
        self.progressData.setObjectName("progressData")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 10, 601, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCreateModel = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonCreateModel.setObjectName("buttonCreateModel")
        self.horizontalLayout.addWidget(self.buttonCreateModel)
        self.buttonBrowseModel = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonBrowseModel.setObjectName("buttonBrowseModel")
        self.horizontalLayout.addWidget(self.buttonBrowseModel)
        self.textModelName = QtWidgets.QLineEdit(self.layoutWidget)
        self.textModelName.setObjectName("textModelName")
        self.horizontalLayout.addWidget(self.textModelName)
        self.buttonUploadModel = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonUploadModel.setObjectName("buttonUploadModel")
        self.horizontalLayout.addWidget(self.buttonUploadModel)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(380, 120, 401, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textXtrain = QtWidgets.QLineEdit(self.layoutWidget1)
        self.textXtrain.setObjectName("textXtrain")
        self.verticalLayout.addWidget(self.textXtrain)
        self.textYtrain = QtWidgets.QLineEdit(self.layoutWidget1)
        self.textYtrain.setObjectName("textYtrain")
        self.verticalLayout.addWidget(self.textYtrain)
        self.textXtest = QtWidgets.QLineEdit(self.layoutWidget1)
        self.textXtest.setObjectName("textXtest")
        self.verticalLayout.addWidget(self.textXtest)
        self.textYtest = QtWidgets.QLineEdit(self.layoutWidget1)
        self.textYtest.setObjectName("textYtest")
        self.verticalLayout.addWidget(self.textYtest)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonXtrain = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonXtrain.setObjectName("buttonXtrain")
        self.verticalLayout_2.addWidget(self.buttonXtrain)
        self.buttonYtrain = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonYtrain.setObjectName("buttonYtrain")
        self.verticalLayout_2.addWidget(self.buttonYtrain)
        self.buttonXtest = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonXtest.setObjectName("buttonXtest")
        self.verticalLayout_2.addWidget(self.buttonXtest)
        self.buttonYtest = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonYtest.setObjectName("buttonYtest")
        self.verticalLayout_2.addWidget(self.buttonYtest)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(380, 340, 401, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonParseData = QtWidgets.QPushButton(self.layoutWidget2)
        self.buttonParseData.setObjectName("buttonParseData")
        self.horizontalLayout_2.addWidget(self.buttonParseData)
        self.buttonSaveData = QtWidgets.QPushButton(self.layoutWidget2)
        self.buttonSaveData.setObjectName("buttonSaveData")
        self.horizontalLayout_2.addWidget(self.buttonSaveData)
        self.buttonUploadData = QtWidgets.QPushButton(self.layoutWidget2)
        self.buttonUploadData.setObjectName("buttonUploadData")
        self.horizontalLayout_2.addWidget(self.buttonUploadData)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(470, 60, 311, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonTestModel = QtWidgets.QPushButton(self.layoutWidget3)
        self.buttonTestModel.setObjectName("buttonTestModel")
        self.horizontalLayout_3.addWidget(self.buttonTestModel)
        self.buttonTrainModel = QtWidgets.QPushButton(self.layoutWidget3)
        self.buttonTrainModel.setObjectName("buttonTrainModel")
        self.horizontalLayout_3.addWidget(self.buttonTrainModel)
        self.buttonSaveModel = QtWidgets.QPushButton(self.layoutWidget3)
        self.buttonSaveModel.setObjectName("buttonSaveModel")
        self.horizontalLayout_3.addWidget(self.buttonSaveModel)
        self.labelCountParams = QtWidgets.QLabel(self.centralwidget)
        self.labelCountParams.setGeometry(QtCore.QRect(20, 60, 171, 16))
        self.labelCountParams.setObjectName("labelCountParams")
        self.textCountParams = QtWidgets.QLabel(self.centralwidget)
        self.textCountParams.setGeometry(QtCore.QRect(200, 60, 47, 20))
        self.textCountParams.setObjectName("textCountParams")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelModel.setText(_translate("MainWindow", "Модель"))
        self.labelData.setText(_translate("MainWindow", "Данные"))
        self.labelTrainCount.setText(_translate("MainWindow", "Образов для обучения:"))
        self.labelTestCount.setText(_translate("MainWindow", "Образов для теста:"))
        self.textTrainCount.setText(_translate("MainWindow", "0"))
        self.textTestCount.setText(_translate("MainWindow", "0"))
        self.buttonCreateModel.setText(_translate("MainWindow", "Create Model"))
        self.buttonBrowseModel.setText(_translate("MainWindow", "Browse Model"))
        self.buttonUploadModel.setText(_translate("MainWindow", "Upload Browsed Model"))
        self.buttonXtrain.setText(_translate("MainWindow", "Browse Parsed Xtrain"))
        self.buttonYtrain.setText(_translate("MainWindow", "Browse Parsed Ytrain"))
        self.buttonXtest.setText(_translate("MainWindow", "Browse Parsed Xtest"))
        self.buttonYtest.setText(_translate("MainWindow", "Browse Parsed Ytest"))
        self.buttonParseData.setText(_translate("MainWindow", "Parse data"))
        self.buttonSaveData.setText(_translate("MainWindow", "Save Parsed Data"))
        self.buttonUploadData.setText(_translate("MainWindow", "Upload Parsed Data"))
        self.buttonTestModel.setText(_translate("MainWindow", "Test Model"))
        self.buttonTrainModel.setText(_translate("MainWindow", "Train Model"))
        self.buttonSaveModel.setText(_translate("MainWindow", "Save Model"))
        self.labelCountParams.setText(_translate("MainWindow", "Количество параметров модели:"))
        self.textCountParams.setText(_translate("MainWindow", "0"))

