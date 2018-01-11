# check information
print(keras.__version__, keras.__file__)
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
print(tf.__version__)
