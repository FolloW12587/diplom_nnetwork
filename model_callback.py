from keras.callbacks import Callback
from tensorflow.keras.callbacks import EarlyStopping
from math import ceil

import settings


class CustomCallback(Callback):
    def __init__(self, form):
        super(CustomCallback, self).__init__()
        self.form = form

    def on_train_begin(self, logs=None):
        self.current = 0
        self.maximum = ceil(self.params['samples'] / settings.BATCH_SIZE) * self.params['epochs']
        progress = self.form.get_progress()
        progress.setMinimum(0)
        progress.setMaximum(self.maximum)
        self.form.progressChanged.emit(self.current)

    def on_batch_end(self, batch, logs):
        self.current += 1
        self.form.progressChanged.emit(self.current)

    def on_epoch_end(self, epoch, logs=None):
        if logs != None and len(logs) != 0:
            if 'accuracy' in logs:
                self.form.accChanged.emit("{:.4f}".format(logs['accuracy']))
            else:    
                self.form.accChanged.emit("{:.4f}".format(logs['mae']))
            self.form.lossChanged.emit("{:.4f}".format(logs['loss']))

    def on_train_end(self, logs=None):
        self.form.progressChanged.emit(self.maximum)
