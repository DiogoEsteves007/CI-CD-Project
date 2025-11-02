from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np
import os
from src.train import train_model

app = FastAPI(title="Pipeline MLOps")

MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/model.joblib"))

train_model()
model = joblib.load(MODEL_PATH)

class Features(BaseModel):
    features: list


@app.get("/")
def read_root():
    return {"message":"API is running!!!"}


@app.post("/predict")
def predict(data: Features):
    pred = model.predict([np.array(data.features)])
    return {"prediction": int(pred[0])}