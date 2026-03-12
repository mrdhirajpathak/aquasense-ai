import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("models/water_model.h5")

def preprocess(image_path):

    img = Image.open(image_path).resize((224,224))

    img = np.array(img) / 255.0

    img = np.expand_dims(img, axis=0)

    return img

def detect_pollution(image_path):

    img = preprocess(image_path)

    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        return "Polluted water detected"
    else:
        return "Water appears clean"
