import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.models.load_model("rice_disease_model.h5")

class_names = ['Bacterialblight', 'Blast', 'Brownspot', 'Tungro']

img_path = "test.jpg"   # replace with your test image

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction)

print("Prediction:", predicted_class)
print("Confidence:", confidence)