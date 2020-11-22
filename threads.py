from PyQt5.QtCore import QThread

import settings
from model_callback import CustomCallback


class TrainModelThread(QThread):
    def __init__(self, data, model, form):
        QThread.__init__(self)
        self.data = data
        self.model = model
        self.form = form

    def __del__(self):
        self.wait()

    def run(self):
        self.history = self.model.fit(self.data[0], self.data[1], 
            batch_size=settings.BATCH_SIZE, 
            epochs=settings.EPOCHS,
            validation_split=settings.VALIDATION_SPLIT,
            verbose=settings.VERBOSE,
            shuffle=True, 
            callbacks=[CustomCallback(self.form),])
