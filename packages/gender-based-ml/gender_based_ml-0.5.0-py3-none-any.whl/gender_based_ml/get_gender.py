# gender.py



from keras.models import load_model
import librosa
import numpy as np
import tensorflow as tf

class GenderPredictor:
    def __init__(self, model_path='./keras_model.h5'):
        self.model = load_model(model_path)
    
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
