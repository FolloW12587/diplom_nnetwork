import pandas as pd
import numpy as np
import random
import os
from scipy.signal import butter, lfilter
from datetime import datetime

import settings


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def normalize(df): #нормализует данные
    return (df - df.mean()) / df.std()

def butter_filter(df, lowcut, highcut, fs, order): #обработка каждого канала df фильтром нижних частот
    new_df = pd.DataFrame()
    for col in df:
        y = butter_bandpass_filter(df[col], lowcut, highcut, fs, order)
        new_df[col] = y
    return new_df

def get_row(dir_name, form): #получить сырые данные
    dirs = os.listdir(dir_name)
    # dirs = dirs[0:2] #уменьшить количество папок для теста парсера
    # ours_path = random.choice(dirs) #рандомно выбирает, чей образ будет свой
    ours_path = dirs[1] #принудительный выбор испытуемого для образа "свой"
    # progress.setMinimum(0)
    # progress.setMaximum(len(dirs))
    form.parseProgressMaximumChanged.emit(len(dirs))
    cur_value = 0
    print('our_path = ', str(ours_path))
    our = []
    alien = []
    for directory in dirs:
        # progress.setValue(cur_value)
        form.parseProgressChanged.emit(cur_value)
        print(str(datetime.now()) + ' ' + directory)
        curr_path = dir_name + '\\' + directory + '\\'
        for i in range(1, len(os.listdir(curr_path))):
            if os.path.exists(curr_path + str(i) + r'.csv'):
                df = pd.read_csv(curr_path + str(i) + r'.csv', skiprows=1, header=None,\
                        names=['COUNTER','INTERPOLATED','AF3','F7','F3','FC5','T7','P7','O1','O2','P8','T8','FC6','F4','F8','AF4','RAW_CQ','GYROX','GYROY','MARKER','MARKER_HARDWARE','SYNC','TIME_STAMP_s','TIME_STAMP_ms','CQ_AF3','CQ_F7','CQ_F3','CQ_FC5','CQ_T7','CQ_P7','CQ_O1','CQ_O2','CQ_P8','CQ_T8','CQ_FC6','CQ_F4','CQ_F8','CQ_AF4','CQ_CMS','CQ_DRL'])
                df = df[['AF3','F7','F3','FC5','T7','P7','O1','O2','P8','T8','FC6','F4','F8','AF4']]
                df = df / 1000
                df = butter_filter(df, 1, 40, 2000, 1)
                #df = normalize(df)
                for j in range(0, len(df), settings.STEP): #разбиваем на выборки по settings.STEP записей c settings.CHANNELS_NUM каналами
                        if j + settings.STEP > len(df):
                            break
                        df_small = df.iloc[j:j + settings.STEP]
                        df_small_n = np.asarray(df_small).transpose()  #.reshape(settings.CHANNELS_NUM, settings.STEP)
                        if directory in ours_path:
                            # our = np.append(our, df_small_n, axis=0)
                            our.append(df_small_n)
                        else:
                            # alien = np.append(alien, df_small_n, axis=0)
                            alien.append(df_small_n)
        cur_value += 1
    # progress.setValue(len(dirs))
    form.parseProgressChanged.emit(cur_value)
    return our, alien


def get_datasets(mass, i):
    len_test = int(len(mass) * settings.PROC)
    len_train = len(mass) - len_test
    mass_train = mass[:len_train]
    # mass_train_y = [i] * len_train
    mass_train_y = [i,] * len_train
    mass_test = mass[len_train:]
    # mass_test_y = [i] * len_test
    mass_test_y = [i,] * len_test
    return mass_train, mass_train_y, mass_test, mass_test_y

def get_data(dir_name, form):
    our, alien = get_row(dir_name, form)
    x_train, y_train, x_test, y_test = split_data(our, alien)
    return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

def split_data(our, alien):
    # our_train, our_train_y, our_test, our_test_y = get_datasets(our, 1)
    # alien_train, alien_train_y, alien_test, alien_test_y = get_datasets(alien, 0)
    
    our_train, our_train_y, our_test, our_test_y = get_datasets(our, settings.KEY_l)
    alien_train, alien_train_y, alien_test, alien_test_y = get_datasets(alien, [0.5]*len(settings.KEY_l))
    x_train = our_train + alien_train
    y_train = our_train_y + alien_train_y
    x_test = alien_test + our_test
    y_test = alien_test_y + our_test_y
    return x_train, y_train, x_test, y_test