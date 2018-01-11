# check keras version/location
print(keras.__version__, keras.__file__)
# for tensorflow
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
# tensorflow version/location
import tensorflow as tf
print(tf.__version__, tf.__file__)

# remove redundant white spaces
a = "bb   cc   dd"
a = " ".join(a.split())
