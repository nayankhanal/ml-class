from fastapi import FastAPI
import joblib, numpy as np
from pydantic import BaseModel

app = FastAPI()

model = joblib.load('linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

class WeightInput(BaseModel):
    weight: float

@app.post("/predict")
def preduct_height(data: WeightInput):
    scaled = scaler.transform([[data.weight]])
    height = model.predict(scaled)[0]
    return {
            "predicted_height": round(float(height), 2)
           }