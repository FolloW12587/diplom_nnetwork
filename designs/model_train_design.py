# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\program_diplom\designs\model_train.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 332)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 381, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelBatchSize = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBatchSize.sizePolicy().hasHeightForWidth())
        self.labelBatchSize.setSizePolicy(sizePolicy)
        self.labelBatchSize.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.labelBatchSize.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelBatchSize.setWordWrap(True)
        self.labelBatchSize.setObjectName("labelBatchSize")
        self.gridLayout.addWidget(self.labelBatchSize, 0, 0, 1, 1)
        self.labelEpochs = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelEpochs.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.labelEpochs.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelEpochs.setWordWrap(True)
        self.labelEpochs.setObjectName("labelEpochs")
        self.gridLayout.addWidget(self.labelEpochs, 1, 0, 1, 1)
        self.textBatchSize = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBatchSize.sizePolicy().hasHeightForWidth())
        self.textBatchSize.setSizePolicy(sizePolicy)
        self.textBatchSize.setMaxLength(300)
        self.textBatchSize.setObjectName("textBatchSize")
        self.gridLayout.addWidget(self.textBatchSize, 0, 1, 1, 1)
        self.labelValidationSplit = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelValidationSplit.sizePolicy().hasHeightForWidth())
        self.labelValidationSplit.setSizePolicy(sizePolicy)
        self.labelValidationSplit.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.labelValidationSplit.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelValidationSplit.setWordWrap(True)
        self.labelValidationSplit.setObjectName("labelValidationSplit")
        self.gridLayout.addWidget(self.labelValidationSplit, 2, 0, 1, 1)
        self.textValidationSplit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textValidationSplit.sizePolicy().hasHeightForWidth())
        self.textValidationSplit.setSizePolicy(sizePolicy)
        self.textValidationSplit.setMaxLength(300)
        self.textValidationSplit.setObjectName("textValidationSplit")
        self.gridLayout.addWidget(self.textValidationSplit, 2, 1, 1, 1)
        self.textEpochs = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEpochs.sizePolicy().hasHeightForWidth())
        self.textEpochs.setSizePolicy(sizePolicy)
        self.textEpochs.setMaxLength(300)
        self.textEpochs.setObjectName("textEpochs")
        self.gridLayout.addWidget(self.textEpochs, 1, 1, 1, 1)
        self.progressTrain = QtWidgets.QProgressBar(Form)
        self.progressTrain.setGeometry(QtCore.QRect(20, 260, 381, 23))
        self.progressTrain.setProperty("value", 0)
        self.progressTrain.setTextVisible(False)
        self.progressTrain.setObjectName("progressTrain")
        self.buttonTrain = QtWidgets.QPushButton(Form)
        self.buttonTrain.setGeometry(QtCore.QRect(170, 290, 75, 23))
        self.buttonTrain.setObjectName("buttonTrain")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLoss = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLoss.sizePolicy().hasHeightForWidth())
        self.labelLoss.setSizePolicy(sizePolicy)
        self.labelLoss.setMinimumSize(QtCore.QSize(85, 0))
        self.labelLoss.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoss.setObjectName("labelLoss")
        self.horizontalLayout.addWidget(self.labelLoss)
        self.textLoss = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLoss.sizePolicy().hasHeightForWidth())
        self.textLoss.setSizePolicy(sizePolicy)
        self.textLoss.setMinimumSize(QtCore.QSize(50, 0))
        self.textLoss.setObjectName("textLoss")
        self.horizontalLayout.addWidget(self.textLoss)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.labelAcc = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAcc.sizePolicy().hasHeightForWidth())
        self.labelAcc.setSizePolicy(sizePolicy)
        self.labelAcc.setMaximumSize(QtCore.QSize(85, 16777215))
        self.labelAcc.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAcc.setWordWrap(True)
        self.labelAcc.setObjectName("labelAcc")
        self.horizontalLayout.addWidget(self.labelAcc)
        self.textAcc = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textAcc.sizePolicy().hasHeightForWidth())
        self.textAcc.setSizePolicy(sizePolicy)
        self.textAcc.setMinimumSize(QtCore.QSize(50, 0))
        self.textAcc.setObjectName("textAcc")
        self.horizontalLayout.addWidget(self.textAcc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelBatchSize.setText(_translate("Form", "Batch_size - количество сэмплов данных после которых будут изменяться веса."))
        self.labelEpochs.setText(_translate("Form", "Epochs - параметр, показывающий сколько раз прогонятся все образы при обучении."))
        self.labelValidationSplit.setText(_translate("Form", "Validation_split - Доля данных обучения, которые будут использоваться в качестве данных проверки."))
        self.buttonTrain.setText(_translate("Form", "Train"))
        self.labelLoss.setText(_translate("Form", "Потери:"))
        self.textLoss.setText(_translate("Form", "0"))
        self.labelAcc.setText(_translate("Form", "Средняя абсолютная ошибка:"))
        self.textAcc.setText(_translate("Form", "0"))

