# check keras version/location
print(keras.__version__, keras.__file__)

# tensorflow version/location
import tensorflow as tf
print(tf.__version__, tf.__file__)

# check devices for tensorflow
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

# remove redundant white spaces
a = "bb   cc   dd"
a = " ".join(a.split())
