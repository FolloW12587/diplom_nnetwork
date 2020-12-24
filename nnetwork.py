import os
import numpy as np
import tensorflow

from tensorflow.keras import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D
from datetime import datetime
from threads import TrainModelThread, ParserThread


import Parser
import settings
from model_callback import CustomCallback


class NNetwork:
    def __init__(self):
        self.model = None
        self.data = None


    def uploadModel(self, file):
        try:
            del self.model
            self.model = load_model(file)
            self.model.summary()
            return self.model.count_params()
        except:
            return False
        return True
    
    def saveModel(self, file_name):
        if file_name:
            self.model.save(file_name, save_format='h5')
            return True
        else:
            return False

    def createModel(self):
        del self.model
        self.model = Sequential()
        self.model.add(Conv1D(64, 5, data_format='channels_first', input_shape=(settings.CHANNELS_NUM, settings.STEP), activation='relu', padding='same'))
        self.model.add(Conv1D(64, 5, activation='relu', padding='same',data_format='channels_first'))
        self.model.add(MaxPooling1D(2,data_format='channels_first'))

        self.model.add(Dropout(0.25))
        self.model.add(Conv1D(128, 5, activation='relu', padding='same',data_format='channels_first'))
        self.model.add(Conv1D(128, 5, activation='relu', padding='same',data_format='channels_first'))
        self.model.add(MaxPooling1D(2,data_format='channels_first'))

        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(1000, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(len(settings.KEY_l), activation='sigmoid'))
        self.model.compile(loss='mse',optimizer="Adam", metrics=["mae"])
        self.model.summary()
        return self.model.count_params()

    def parseData(self, dir_name, form):
        if self.data:
            return False
        return ParserThread(dir_name, form)

    def getParsedData(self, progress, x_train_name, y_train_name, x_test_name=None, y_test_name=None):
        if self.data:
            return False
        output = []
        x_data = self.getDataByFileName(x_train_name)
        progress.setValue(1)
        y_data = self.getDataByFileName(y_train_name)
        progress.setValue(2)
        if x_test_name and y_test_name:
            output.append(x_data)
            x_test = self.getDataByFileName(x_test_name)
            progress.setValue(3)
            output.append(y_data)
            output.append(x_test)
            y_test = self.getDataByFileName(y_test_name)
            progress.setValue(4)
            output.append(y_test)
            self.data = tuple(output)
            return True
        else:
            x_train, y_train, x_test, y_test = Parser.split_data(x_data, y_data)
            progress.setValue(4)
            self.data = (np.array(x_train), y_train, np.array(x_test), y_test)
            return True

    def getDataByFileName(self, file_name):
        return np.load(file_name)

    def saveParsedData(self, dir_name):
        if self.data != None:
            np.save(dir_name + r'\x_train', self.data[0])
            np.save(dir_name + r'\y_train', self.data[1])
            np.save(dir_name + r'\x_test', self.data[2])
            np.save(dir_name + r'\y_test', self.data[3])

    def trainModel(self, form):
        if self.data and self.model:
            return TrainModelThread(self.data, self.model, form)

    def testModel(self, form):
        self.testOnData(self.data[0], self.data[1], form, 'train')
        self.testOnData(self.data[2], self.data[3], form, 'test')


    def score_errors(self, prediction, y, form, data_type):
        first_all = 0
        first_false = 0
        first_acc = 0
        first_max_acc = 0
        second_all = 0
        second_false = 0
        second_acc = 0
        second_max_acc = 0
        second_hd_avg = 0
        second_hd_max = 0
        second_hd_min = 1

        for i in range(len(prediction)): 
            s = self.Hemming_distance(np.array(y[i]), np.array(prediction[i]))
            
            acc = (1 - s/len(settings.KEY_l))
            if (y[i] == np.array(settings.KEY_l)).all():
                first_all += 1
                first_acc += acc
                if acc > first_max_acc:
                    first_max_acc = acc
                if s > 0:
                    first_false += 1
            else:
                second_all += 1
                second_acc += acc
                if acc > second_max_acc:
                    second_max_acc = acc
                
                d = self.Hemming_distance(np.array(prediction[i]), np.array(settings.KEY_l))/len(settings.KEY_l)
                second_hd_avg += d
                if d > second_hd_max:
                    second_hd_max = d
                if d < second_hd_min:
                    second_hd_min = d
                if d == 0:
                    second_false += 1

        first_error = first_false / first_all
        second_error = second_false / second_all
        first_acc_avg = first_acc / first_all
        second_acc_avg = second_acc / second_all
        second_hd_avg = second_hd_avg / second_all

        form_fields = form.getFormFields(data_type)
        if len(form_fields) != 0:
            form_fields[0].setText("{:d}".format(len(prediction)))
            form_fields[1].setText("{:d}".format(first_all))
            form_fields[2].setText("{:d}".format(first_false))
            form_fields[3].setText("{:.5f}".format(first_error))
            form_fields[4].setText("{:.5f}".format(first_acc_avg))
            form_fields[5].setText("{:d}".format(second_all))
            form_fields[6].setText("{:d}".format(second_false))
            form_fields[7].setText("{:.5f}".format(second_error))
            form_fields[8].setText("{:.5f}".format(second_hd_avg))

        print("Количество тестовых данных = ", len(prediction))
        print('Полное количество "своих" = {a:d}, количество ложных срабатываний = {f:d}, отношение ложных срабатываний к всем "своим" = {e:.5f}, средняя точность = {a_a:.5f}, max_acc = {m_a:.5f}'.format(a = first_all, f = first_false, e=first_error, a_a=first_acc_avg, m_a=first_max_acc))
        print('Полное количество "чужих" = {a:d}, количество ложных пропусков = {f:d}, отношение ложных пропусков ко всем "чужим" = {e:.5f}, среднее расстояние Хемминга = {hd_a:.5f}, max расстояние Хемминга = {hd_max:.5f}, min расстояние Хемминга = {hd_min:.5f}'.format(a=second_all, f=second_false, e=second_error, hd_a=second_hd_avg, hd_max=second_hd_max, hd_min=second_hd_min))

    def testOnData(self, x, y, form, data_type):
        scores = self.model.evaluate(x, y)
        prediction = self.model.predict(x)
        self.score_errors(prediction, y, form, data_type)

    def Hemming_distance(self, x, y): 
        d = np.greater(np.abs(x - y), [settings.MODUL / 2]*len(x)).astype('int')
        return np.sum(d)

    def getKeyOfImage(self, test_image):
        prediction = self.model.predict(np.array([test_image,]))
        return self.get_key_from_list(prediction[0])

    def get_key_from_list(self, l):
        key_str = ''
        for c in l:
            m = c % settings.MODUL
            key_code = (c - m)/settings.MODUL
            if m >= settings.MODUL / 2:
                key_code += 1
            key_str += settings.APLHABET[int(key_code)]
        return key_str

    def get_one_image(self, file_name):
        return Parser.parse_one_image_from_file(file_name)