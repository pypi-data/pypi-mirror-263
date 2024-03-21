# gender.py



from keras.models import load_model
import librosa
import numpy as np
import tensorflow as tf
import os

class GenderPredictor:
    # def __init__(self, model_path='./keras_model.h5'):
    #     #self.model = load_model(model_path)
    #     self.model = self.load_gender_model()
    path=r'C:\\Users\\PriyaBegurSrikantapr\\Repos\\SP\\gender_based_ml\\gender_based_ml\\keras_model.h5'
    def __init__(self, model_path=None):
        if model_path is None:
            # Default model path within the library package
            # Get the directory of the current script
            current_dir = os.path.dirname(__file__)
            #model_path = os.path.join(os.path.dirname(__file__), 'gender_based_ml', 'keras_model.h5')
            model_path = os.path.join(current_dir, 'gender_based_ml', 'keras_model.h5')
        self.model = load_model(model_path)
    
    # def load_gender_model():
    #     model_path = os.path.join(os.path.dirname(__file__), 'models', 'gender_model.h5')
    #     return load_model(model_path)
    
    def predict_gender(self, audio_file_path):
        # Load the audio file and extract MFCC features
        wf, sr = librosa.load(audio_file_path)
        mfcc_wf = librosa.feature.mfcc(y=wf, sr=sr)
        
        # Pad the MFCC features and prepare for prediction
        b = tf.keras.utils.pad_sequences(mfcc_wf, padding='post', maxlen=200)
        
        # Make prediction
        prediction = self.model.predict(np.array([b]))
        
        # Define threshold and classify gender
        threshold = 0.5
        if prediction >= threshold:
            gender = "Male"
        else:
            gender = "Female"
        
        return gender
