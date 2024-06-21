import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os




class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    @tf.function  # Ensures the function is traced once
    def predict_image(self, model, test_image):
        return model.predict(test_image)

    def predict(self):
        # Load the model without compiling to avoid the warning
        model = load_model(os.path.join("model", "model.h5"), compile=False)

        # Prepare the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Get prediction
        result = np.argmax(self.predict_image(model, test_image), axis=1)

        print('Here is the result:', result)

        if result[0] == 1:
            prediction = 'Tumor'
        else:
            prediction = 'Normal'
        
        return [{"image": prediction}]

# Example usage:
# pipeline = PredictionPipeline('path/to/your/image.jpg')
# prediction = pipeline.predict()
# print(prediction)
