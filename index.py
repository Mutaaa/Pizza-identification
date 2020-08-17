# import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

img_height = 180
img_width = 180

model = tf.keras.models.load_model('./pizza_model')

print('\n\n\n')

# Check its architecture
# model.summary()

class_names = [ 'not-pizza', 'pizza' ]

target_dir = './pizza/'
images = os.listdir(target_dir)

for img_path in images:
    target_image_path = target_dir + img_path
    # print(img)
    img = keras.preprocessing.image.load_img(
        target_image_path, target_size=(img_height, img_width)
    )

    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "{} is belongs to {} with a {:.2f} percent confidence."
        .format(img_path, class_names[np.argmax(score)], 100 * np.max(score))
    )