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

def butter_filter(df, lowcut, highcut, fs, order): # обработка каждого канала df фильтром нижних частот
    new_df = pd.DataFrame()
    for col in df:
        y = butter_bandpass_filter(df[col], lowcut, highcut, fs, order)
        new_df[col] = y
    return new_df

def get_row(dir_name, form):             # получить сырые данные
    dirs = os.listdir(dir_name)

    if settings.LIMIT_DATA_TESTEE_COUNT: # уменьшить количество папок для теста парсера, если включена данная настройка
        dirs = dirs[0:settings.LIMIT_DATA_TESTEE_COUNT]      
                  
    ours_path = random.choice(dirs)      # случайно выбирает, чей образ будет свой
    form.parseProgressMaximumChanged.emit(len(dirs))
    cur_value = 0
    print('our_path = ', str(ours_path))
    our = []
    alien = []
    for directory in dirs:
        form.parseProgressChanged.emit(cur_value)
        print(str(datetime.now()) + ' ' + directory)
        curr_path = dir_name + '\\' + directory + '\\'
        data = get_data_from_dir(curr_path)
        if directory == ours_path:
            our += data
        else: 
            alien += data
        cur_value += 1
    form.parseProgressChanged.emit(cur_value)
    return our, alien

def get_data_from_dir(path_name, num=0):
    output = []
    if num:
        count = 0
    for i in range(1, len(os.listdir(path_name))):
        if os.path.exists(path_name + str(i) + r'.csv'):
            df = pd.read_csv(path_name + str(i) + r'.csv', skiprows=1, header=None,\
                    names=['COUNTER','INTERPOLATED','AF3','F7','F3','FC5','T7','P7','O1','O2','P8','T8','FC6','F4','F8','AF4','RAW_CQ','GYROX','GYROY','MARKER','MARKER_HARDWARE','SYNC','TIME_STAMP_s','TIME_STAMP_ms','CQ_AF3','CQ_F7','CQ_F3','CQ_FC5','CQ_T7','CQ_P7','CQ_O1','CQ_O2','CQ_P8','CQ_T8','CQ_FC6','CQ_F4','CQ_F8','CQ_AF4','CQ_CMS','CQ_DRL'])
            df = df[['AF3','F7','F3','FC5','T7','P7','O1','O2','P8','T8','FC6','F4','F8','AF4']]
            df = df / 1000
            df = butter_filter(df, 1, 40, 2000, 1)
            for j in range(0, len(df), settings.STEP): # разбиваем на выборки по settings.STEP записей c settings.CHANNELS_NUM каналами
                if j + settings.STEP > len(df):
                    break
                df_small = df.iloc[j:j + settings.STEP]
                df_small = np.asarray(df_small).transpose()  
                output.append(df_small)
                
                if num:
                    count += 1
                    if count >= num:
                        return output
    return output

def get_datasets(mass, i):
    len_test = int(len(mass) * settings.PROC)
    len_train = len(mass) - len_test
    mass_train = mass[:len_train]
    mass_train_y = [i,] * len_train
    mass_test = mass[len_train:]
    mass_test_y = [i,] * len_test
    return mass_train, mass_train_y, mass_test, mass_test_y

def get_data(dir_name, form):
    our, alien = get_row(dir_name, form)
    x_train, y_train, x_test, y_test = split_data(our, alien)
    return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

def split_data(our, alien):
    our_train, our_train_y, our_test, our_test_y = get_datasets(our, settings.KEY_l)
    alien_train, alien_train_y, alien_test, alien_test_y = get_datasets(alien, [0.5]*len(settings.KEY_l))
    x_train = our_train + alien_train
    y_train = our_train_y + alien_train_y
    x_test = alien_test + our_test
    y_test = alien_test_y + our_test_y
    return x_train, y_train, x_test, y_test
