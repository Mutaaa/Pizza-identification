import numpy as np
import os
import uuid
import json
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

from flask import Flask, request
from flask_restful import Resource, Api

img_height = 180
img_width = 180

model = tf.keras.models.load_model('./pizza_model')
class_names = [ 'not-pizza', 'pizza' ]

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join('/app/upload/', f_name))
        
        img = keras.preprocessing.image.load_img(
            '/app/upload/' + f_name, target_size=(img_height, img_width)
        )

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        class_name = class_names[np.argmax(score)]
        score = 100 * np.max(score)
        
        return json.dumps({'class':class_name, 'score': score})

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')