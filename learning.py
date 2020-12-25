from PyQt5 import QtWidgets, QtCore
from designs.learning_design import Ui_MainWindow  
from designs.parser_design import Ui_Form as Ui_Form_parser
from designs.model_train_design import Ui_Form as Ui_Form_model_train
from designs.model_test_design import Ui_Form as Ui_Form_model_test
import sys
import os

from nnetwork import NNetworkLearning
import settings 


class parserForm(QtWidgets.QWidget):
    def __init__(self, main_window):
        super(parserForm, self).__init__()
        self.ui = Ui_Form_parser()
        self.ui.setupUi(self)

        self.main_window = main_window
        self.ui.textProc.setText(str(settings.PROC))
        self.ui.textStep.setText(str(settings.STEP))

        self.ui.buttonBrowseDataFolder.clicked.connect(self.browseParseData)
        self.ui.buttonParseData.clicked.connect(self.parseData)

        
    def browseParseData(self):
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.ui.textBrowseDataFolder.setText(dir_name)

    def parseData(self):
        try:
            settings.PROC = float(self.ui.textProc.text())
            settings.STEP = int(self.ui.textStep.text())
            dir_name = self.ui.textBrowseDataFolder.text()
            self.ui.buttonParseData.setEnabled(False)
            self.main_window.parseData(dir_name)
        except ValueError:
            self.ui.buttonParseData.setEnabled(True)
            self.showErrorDialog("Incorrect values!")

    def showErrorDialog(self, message):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage(message)


class modelTestForm(QtWidgets.QWidget):
    def __init__(self):
        super(modelTestForm, self).__init__()
        self.ui = Ui_Form_model_test()
        self.ui.setupUi(self)

    def getFormFields(self, data_type):
        if data_type == 'train':
            return [
                self.ui.textTrainCount,
                self.ui.textTrainCountOurs,
                self.ui.textTrainOursError,
                self.ui.textTrainRatioError,
                self.ui.textTrainAvgAcc,
                self.ui.textTrainCountAliens,
                self.ui.textTrainAliensError,
                self.ui.textTrainAliensRatioError,
                self.ui.textTrainHemmingDistance,
            ]
        elif data_type == 'test':
            return[
                self.ui.textTestCount,
                self.ui.textTestCountOurs,
                self.ui.textTestOursError,
                self.ui.textTestRatioError,
                self.ui.textTestAvgAcc,
                self.ui.textTestCountAliens,
                self.ui.textTestAliensError,
                self.ui.textTestAliensRatioError,
                self.ui.textTestHemmingDistance,
            ]
        else:
            return []


class modelTrainForm(QtWidgets.QWidget):
    progressChanged = QtCore.pyqtSignal(int)
    lossChanged = QtCore.pyqtSignal(str)
    accChanged = QtCore.pyqtSignal(str)
    
    def __init__(self, main_window):
        super(modelTrainForm, self).__init__()
        self.ui = Ui_Form_model_train()
        self.ui.setupUi(self)

        self.main_window = main_window
        self.ui.textBatchSize.setText(str(settings.BATCH_SIZE))
        self.ui.textEpochs.setText(str(settings.EPOCHS))
        self.ui.textValidationSplit.setText(str(settings.VALIDATION_SPLIT))

        self.ui.buttonTrain.clicked.connect(self.trainModel)
        self.progressChanged.connect(self.ui.progressTrain.setValue)
        self.lossChanged.connect(self.ui.textLoss.setText)
        self.accChanged.connect(self.ui.textAcc.setText)

    def trainModel(self):
        try:
            settings.BATCH_SIZE = int(self.ui.textBatchSize.text())
            settings.EPOCHS = int(self.ui.textEpochs.text())
            settings.VALIDATION_SPLIT = float(self.ui.textValidationSplit.text())
            self.ui.buttonTrain.setEnabled(False)
            self.main_window.trainModel()
        except ValueError as e:
            self.ui.buttonTrain.setEnabled(True)
            self.showErrorDialog("Incorrect values!")

    def get_progress(self):
        return self.ui.progressTrain
            
    def showErrorDialog(self, message):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage(message)

 
class mywindow(QtWidgets.QMainWindow):
    parseProgressChanged = QtCore.pyqtSignal(int)
    parseProgressMaximumChanged = QtCore.pyqtSignal(int)
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.parserForm = parserForm(self)
        self.modelTrainForm = modelTrainForm(self)
        self.modelTestForm = modelTestForm()

        self.nnetwork = NNetworkLearning()

        self.ui.buttonBrowseModel.clicked.connect(self.browseModel)
        self.ui.buttonUploadModel.clicked.connect(self.uploadModel)
        self.ui.buttonSaveModel.clicked.connect(self.saveModel)
        self.ui.buttonCreateModel.clicked.connect(self.createModel)
        self.ui.buttonTrainModel.clicked.connect(self.trainModelAction)
        self.ui.buttonTestModel.clicked.connect(self.testModel)

        self.ui.buttonParseData.clicked.connect(self.parseDataAction)
        self.ui.buttonSaveData.clicked.connect(self.saveParsedData)
        self.ui.buttonUploadData.clicked.connect(self.uploadData)

        self.ui.buttonXtrain.clicked.connect(lambda: self.browseDataFile(self.ui.textXtrain))
        self.ui.buttonYtrain.clicked.connect(lambda: self.browseDataFile(self.ui.textYtrain))
        self.ui.buttonXtest.clicked.connect(lambda: self.browseDataFile(self.ui.textXtest))
        self.ui.buttonYtest.clicked.connect(lambda: self.browseDataFile(self.ui.textYtest))
        self.parseProgressChanged.connect(self.ui.progressData.setValue)
        self.parseProgressMaximumChanged.connect(self.ui.progressData.setMaximum)


    def browseModel(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.ui.textModelName.setText(fname)

    def uploadModel(self):
        file_name = self.ui.textModelName.text()
        try:
            f = open(file_name, 'r')
            f.close()
            count_params = self.nnetwork.uploadModel(file_name)
            if not count_params:
                self.showErrorDialog('Error in loading model!')
            self.ui.textCountParams.setText("{:d}".format(count_params))
        except FileNotFoundError:
            self.showErrorDialog('File not found!')
            self.ui.textModelName.setText('')
        except IOError:
            self.showErrorDialog('File cannot be read!')

    def showErrorDialog(self, message):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage(message)

    def saveModel(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'mymodel')[0]
        if not self.nnetwork.saveModel(file_name):
            self.showErrorDialog('Error in saving model!')

    def createModel(self):
        count_params = self.nnetwork.createModel()
        self.ui.textCountParams.setText("{:d}".format(count_params))

    def parseDataAction(self):
        if self.parserForm:
            self.parserForm.show()

    def destoyParseWindow(self):
        self.parserForm = None

    def parseData(self, dir_name):
        self.parseTread = self.nnetwork.parseData(dir_name, self)
        if not self.parseTread:
            self.parseTread = None
            self.showErrorDialog('Error in parsing data')
        else:
            self.parseTread.finished.connect(self.parseFinished)
            self.parseTread.start()
            
    def parseFinished(self):
        self.nnetwork.data = self.parseTread.data
        self.ui.textTrainCount.setText(str(len(self.nnetwork.data[0])))
        self.ui.textTestCount.setText(str(len(self.nnetwork.data[2])))
        self.destoyParseWindow()

    def saveParsedData(self):
        if not self.nnetwork.data:
            return
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.nnetwork.saveParsedData(dir_name)

    def uploadData(self):
        self.ui.progressData.setMinimum(0)
        self.ui.progressData.setMaximum(4)
        self.ui.progressData.setValue(0)
        if not self.nnetwork.getParsedData(
            self.ui.progressData,
            self.ui.textXtrain.text(),
            self.ui.textYtrain.text(),
            self.ui.textXtest.text(),
            self.ui.textYtest.text()
        ):
            self.showErrorDialog('Data is uploaded!')
            self.ui.progressData.setValue(4)
            return
        self.ui.textTrainCount.setText(str(len(self.nnetwork.data[0])))
        self.ui.textTestCount.setText(str(len(self.nnetwork.data[2])))
        
    def browseDataFile(self, widget):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        widget.setText(fname)

    def trainModelAction(self):
        if self.modelTrainForm:
            self.modelTrainForm.show()

    def trainModel(self):
        if not self.nnetwork.model or not self.nnetwork.data:
            self.showErrorDialog('You should upload data and model!')
            return
        self.thread = self.nnetwork.trainModel(self.modelTrainForm)
        self.thread.finished.connect(self.trainFinished)
        self.thread.start()

    def trainFinished(self):
        self.modelTrainForm.ui.buttonTrain.setEnabled(True)
        self.nnetwork.history = self.thread.history
        self.modelTrainForm.hide()
        self.testModel()

    def testModel(self):
        if not self.nnetwork.data or not self.nnetwork.model:
            self.showErrorDialog('You should upload data and model!')
            return
        self.modelTestForm.show()
        self.nnetwork.testModel(self.modelTestForm)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())