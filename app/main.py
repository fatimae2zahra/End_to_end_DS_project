from fastapi import FastAPI
from app.utils.model import load_model, predict

app = FastAPI()

# Load model
model = load_model()


@app.get("/")
def read_root():
    return {
        """
        message": "Welcome to my first API based on model requests!
        Besos
        Fatima-Ezzahra
        """
    }


@app.post("/predict")
def predict_api(payload: dict):
    prediction = predict(model, payload)
    return {"prediction": prediction}
