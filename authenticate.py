from PyQt5 import QtWidgets, QtCore
from designs.authentication_design import Ui_MainWindow  
from designs.is_authenticated_design import Ui_Form as Ui_Form_is_authenticated
import sys
import os

from nnetwork import NNetworkAuth
import settings 


class isAuthenticatedForm(QtWidgets.QWidget):
    def __init__(self, key, is_authenticated):
        super(isAuthenticatedForm, self).__init__()
        self.ui = Ui_Form_is_authenticated()
        self.ui.setupUi(self)

        self.key = key[0:86] + ' ' + key[86:172] + ' ' + key[172:]
        self.ui.textKey.setText(self.key)
        if (is_authenticated):
            self.ui.textIsAuthenticated.setText("Вы успешно прошли аутентификацию!")
        else:
            self.ui.textIsAuthenticated.setText("Вы не прошли аутентификацию!")


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.isAuthenticatedForm = None
        self.nnetwork = NNetworkAuth()
        self.test_image = None

        self.ui.buttonBrowseModel.clicked.connect(self.browseModel)
        self.ui.buttonUploadModel.clicked.connect(self.uploadModel)
        self.ui.buttonBrowseDataFolder.clicked.connect(self.browseDataFolder)
        self.ui.buttonUploadImages.clicked.connect(self.uploadImages)
        self.ui.buttonAuthenticate.clicked.connect(self.authenticate)


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
                return
            self.ui.textCountParams.setText("{:d}".format(count_params))
        except FileNotFoundError:
            self.showErrorDialog('File not found!')
            self.ui.textModelName.setText('')
        except IOError:
            self.showErrorDialog('File cannot be read!')
    
    def browseDataFolder(self):
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.ui.textDataFileName.setText(dir_name)
    
    def uploadImages(self):
        self.test_image = None
        self.ui.textDataUploaded.setText('Нет')
        
        file_name = self.ui.textDataFileName.text()
        self.test_image = self.nnetwork.get_some_images(file_name + '\\', settings.COUNT_IMAGES_FOR_TEST)
        if self.test_image is None:
            self.showErrorDialog('Error in getting image!')
            return

        self.ui.textDataUploaded.setText('Да')


    def authenticate(self):
        if self.test_image is None:
            self.showErrorDialog('You should upload image first!')
            return

        if not self.nnetwork.model:
            self.showErrorDialog('You should upload model first!')
            return

        key = self.nnetwork.getKeyOfSetOfImages(self.test_image)
        if not key:
            self.showErrorDialog('Error in authentification!')
            return
        
        key_l = list(map(lambda x: int(x), key))
        if key_l == settings.KEY_l:
            self.isAuthenticatedForm = isAuthenticatedForm(key, True)
        else: 
            self.isAuthenticatedForm = isAuthenticatedForm(key, False)

        self.isAuthenticatedForm.show()

    def showErrorDialog(self, message):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage(message)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())