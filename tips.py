# to check nvidia gpu information, use
#nvidia-smi

# check keras version/location
print(keras.__version__, keras.__file__)

# tensorflow version/location
import tensorflow as tf
print(tf.__version__, tf.__file__)

# check devices for tensorflow
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

# Only make one GPU visible to Tensorflow so that it does not allocate
# all available memory on all devices.
# See: https://stackoverflow.com/questions/37893755
os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

# remove redundant white spaces
a = "bb   cc   dd"
a = " ".join(a.split())

# https://stackoverflow.com/questions/44466066/how-can-i-convert-a-trained-tensorflow-model-to-keras
# The ckpt file can be saved by TF with:
saver = tf.train.Saver()
saver.save(sess, checkpoint_name)

#and to load checkpoint in Keras, you need a callback class as follow:
class MyCallbacks(keras.callbacks.Callback):
    def __init__(self, pretrained_file):
        self.pretrained_file = pretrained_file
        self.sess = keras.backend.get_session()
        self.saver = tf.train.Saver()
    def on_train_begin(self, logs=None):
        if self.pretrian_model_path:
            self.saver.restore(self.sess, self.pretrian_model_path)
            print('load weights: OK.')

 #Then in your keras script:
 model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
 testCallBack = MyCallbacks(pretrian_model_path='./XXXX.ckpt') 
 model.fit(x_train, y_train, batch_size=128, epochs=20, callbacks=[testCallBack])
