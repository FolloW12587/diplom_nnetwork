import os
import pandas as pd
import numpy as np
import tensorflow
# print(tensorflow.__version__)
from tensorflow.keras import Sequential
# from keras.models import Sequential, load_model
from keras.models import load_model
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers.convolutional import Conv1D, MaxPooling1D
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D
# from tensorflow.keras.layers.convolutional import Conv1D, MaxPooling1D
from datetime import datetime
from threads import TrainModelThread


import Parser
import settings
from model_callback import CustomCallback
from custom_losses import CustomBinaryCrossEntropy


class NNetwork:
    def __init__(self):
        self.model = None
        self.data = None


    def uploadModel(self, file):
        try:
            self.model = load_model(file)
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
        # tensorflow.config.run_functions_eagerly(True)
        # print(tensorflow.executing_eagerly())
        self.model = None
        self.model = Sequential()
        self.model.add(Conv1D(64, 5, data_format='channels_first', input_shape=(settings.CHANNELS_NUM, settings.STEP), activation='relu', padding='same'))
        self.model.add(Conv1D(64, 5, activation='relu', padding='same',data_format='channels_first'))
        self.model.add(MaxPooling1D(2,data_format='channels_first'))
        # Слой регуляризации Dropout
        self.model.add(Dropout(0.25))
        self.model.add(Conv1D(128, 5, activation='relu', padding='same',data_format='channels_first'))
        self.model.add(Conv1D(128, 5, activation='relu', padding='same',data_format='channels_first'))
        self.model.add(MaxPooling1D(2,data_format='channels_first'))
        # Слой регуляризации Dropout
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(1000, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(len(settings.KEY_l), activation='sigmoid'))
        # self.model.add(Dense(1, activation='sigmoid'))
        # self.model.run_eagerly = True
        # self.model.compile(loss='binary_crossentropy',optimizer="SGD", metrics=["accuracy"]) #  run_eagerly=True
        self.model.compile(loss='mse',optimizer="Adam", metrics=["mae"]) #  run_eagerly=True
        self.model.summary()

    def parseData(self, dir_name, progress):
        if self.data:
            return False
        self.data = Parser.get_data(dir_name, progress)
        return True

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
            # self.history = self.model.fit(self.data[0], self.data[1], 
            #     batch_size=settings.BATCH_SIZE, 
            #     epochs=settings.EPOCHS,
            #     validation_split=settings.VALIDATION_SPLIT,
            #     verbose=settings.VERBOSE,
            #     shuffle=True, 
            #     callbacks=[CustomCallback(progress, loss, acc),])
            return TrainModelThread(self.data, self.model, form)

    def testModel(self):
        self.testOnData(self.data[2], self.data[3])

        # x = np.append(self.data[0].transpose(), self.data[2].transpose(), axis=len(self.data[0].shape) - 1)
        # x = x.transpose()
        # y = np.append(self.data[1], self.data[3])
        # self.testOnData(x, y)
        self.testOnData(self.data[0], self.data[1])


    def score_errors(self, prediction, y):
        first_all = 0
        first_false = 0
        first_acc = 0
        first_max_acc = 0
        second_all = 0
        second_false = 0
        second_acc = 0
        second_max_acc = 0
        for i in range(len(prediction)):
            d = np.less(np.abs(np.array(y[i]) - np.array(prediction[i])), [settings.MODUL / 2]*len(settings.KEY_l)).astype('int')
            s = np.sum(d)
            
            acc = s/len(settings.KEY_l)
            if (y[i] == np.array(settings.KEY_l)).all():
                first_all += 1
                first_acc += acc
                if acc > first_max_acc:
                    first_max_acc = acc
                if s < len(settings.KEY_l):
                    first_false += 1
            else:
                second_all += 1
                second_acc += acc
                if acc > second_max_acc:
                    second_max_acc = acc
                if (np.array(prediction[i]) == np.array(settings.KEY_l)).all():
                    second_false += 1

        first_error = first_false / first_all
        second_error = second_false / second_all
        first_acc_avg = first_acc / first_all
        second_acc_avg = second_acc / second_all

        print("Количество тестовых данных = ", len(prediction))
        print('Полное количество "своих" = {a}, количество ложных срабатываний = {f}, отношение ложных срабатываний к всем "своим" = {e}, средняя точность = {a_a}, max_acc = {m_a}'.format(a = first_all, f = first_false, e=first_error, a_a=first_acc_avg, m_a=first_max_acc))
        print('Полное количество "чужих" = {a}, количество ложных пропусков = {f}, отношение ложных пропусков ко всем "чужим" = {e}, средняя точность = {a_a}, max_acc = {m_a}'.format(a = second_all, f = second_false, e=second_error, a_a=second_acc_avg, m_a=second_max_acc))

    def testOnData(self, x, y):
        scores = self.model.evaluate(x, y)
        print("Доля верных ответов на тестовых данных, в процентах:", round(scores[1] * 100, 4))
        prediction = self.model.predict(x)
        self.score_errors(prediction, y)