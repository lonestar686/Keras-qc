# Demonstrates the use of Numpy Digitize to convert predictions into Categories
# http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.digitize.html

import numpy as np

preds = [1.22, 3.32, 6.54, 3.22, 6.78, 8.1, 2.01]
splits = [0, 1.5, 2.5, 3, 4.2, 5.8, 6.5, 7]

response = np.digitize(preds, splits)

print(response)

# to initialize seeds
random_seed = 2018
random.seed(random_seed)
import numpy as np
np.random.seed(random_seed)
import tensorflow as tf
tf.set_random_seed(random_seed)
