PROC = 0.3                      # percentage of the train and test data split
STEP = 1024                     # size of the data image
LIMIT_DATA_TESTEE_COUNT = 0     # limit test persons for parse. If zero there is no limit.
COUNT_IMAGES_FOR_TEST = 10      # count of images that would be parsed in attempt of authentication
CHANNELS_NUM = 14               # number of channels in image
BATCH_SIZE=32                   # batch size of trainig data
EPOCHS=25                       # number of training iterations
VALIDATION_SPLIT=0.2            # percentage of the validation data while training
VERBOSE=1                       # show progress in console
APLHABET = r"01"                # key's alphabet
APLHABET_LEN = len(APLHABET)
MODUL = 1/(APLHABET_LEN - 1)

KEY_l = [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0,\
    1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0,\
    0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1,\
    1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1,\
    1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0,\
    1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1
]                               # key for our's images