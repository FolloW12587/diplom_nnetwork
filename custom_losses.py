from keras import losses
import tensorflow as tf
import keras.backend as K
import numpy as np

import settings

DELTA = settings.MODUL / 2


def Hemming_distance(y_true, y_pred):
    # d = [0]*settings.BATCH_SIZE
    # for i in range(settings.BATCH_SIZE):
    #     for j in range(len(settings.KEY_l)):
    #         if k.y_pred[i,j] >= y_true[i][j] - DELTA and y_pred[i][j] < y_true[i][j] + DELTA:
    #             d[i] += 1
    # return np.array(d) / len(y_pred)

    b = K.less(K.abs(y_pred - np.array([settings.KEY_l,]*settings.BATCH_SIZE)), DELTA)
    return tf.math.count_nonzero(b, 1)/len(settings.KEY_l)

def get_answers(y_true):
    # r = []
    # for i in range(settings.BATCH_SIZE):
    #     res = K.all(settings.KEY_l == y_true[i])
    #     a = 0 if res else 1
    #     r.append(a)
    # return np.array(r)
    b = K.all(K.equal(y_true, settings.KEY_l), 1)
    return K.cast(b, 'float64')


def CustomBinaryCrossEntropy(y_true, y_pred):
    # test = np.array(y_pred)
    # print(test)
    d = Hemming_distance(y_true, y_pred)
    r = get_answers(y_true)
    return losses.binary_crossentropy(r, d)
    # return losses.binary_crossentropy(y_true, y_pred)