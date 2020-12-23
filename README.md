# diplom_nnetwork

## System requirements

* Python 3.5–3.8
* pip 19.0 or later (requires manylinux2010 support)
* Ubuntu 16.04 or later (64-bit)
* macOS 10.12.6 (Sierra) or later (64-bit) (no GPU support)
* Windows 7 or later (64-bit)
* Raspbian 9.0 or later.
* GPU support requires a CUDA®-enabled card (Ubuntu and Windows)

## Installation

Clone the repopsitory:
    git clone git@github.com:FolloW12587/diplom_nnetwork.git

Install the dependencies:
    pip install -r requirements.txt

## Settings

All settings are in the `settings.py` file. Here're the default settings
```python
PROC = 0.3                      # percentage of the train and test data split
STEP = 1024                     # size of the data image
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
```

## Usage

If you haven't got trained model. You can do it with `learning.py` module:
    python learning.py

When you got your model you can use it with `authenticate.py` module:
    python authenticate.py