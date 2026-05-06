from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

model = tf.keras.models.load_model("rice_disease_model.h5")

class_names = ['Bacterialblight', 'Blast', 'Brownspot', 'Tungro']

solutions = {
    "Bacterialblight": "Apply appropriate bactericide and improve field drainage.",
    "Blast": "Use fungicide such as Tricyclazole.",
    "Brownspot": "Apply Mancozeb fungicide and balanced fertilizer.",
    "Tungro": "Control insect vectors and remove infected plants."
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    filepath = os.path.join("static", file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    solution = solutions[predicted_class]

    return render_template(
    'index.html',
    prediction=predicted_class,
    solution=solution,
    image_path=filepath
)


if __name__ == '__main__':
    app.run(debug=True)