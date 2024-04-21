import joblib
import pandas as pd


def load_model():
    model_path = "models/trained_model.pkl"
    model = joblib.load(model_path)
    return model


def predict(model, data):
    ss = joblib.load("models/StandardScaler.pkl")
    features_transformed = ss.transform(pd.DataFrame([data]))
    prediction_transformed = model.predict(features_transformed)
    le = joblib.load("models/LabelEncoder.pkl")
    prediction = le.inverse_transform(prediction_transformed)[0]
    return prediction
