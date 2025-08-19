from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load(r"C:\Users\Alec\Desktop\Projects\valmine\Analysis\model.pkl")

app = FastAPI()

class PredictRequest(BaseModel):
    econ_rating: float
    headshot_percentage: float
    headshots: int
    damage: int


@app.post("/predict")
def predict(request: PredictRequest):
    features = np.array([[
        request.econ_rating,
        request.headshot_percentage,
        request.headshots,
        request.damage
    ]])
    
    prediction = model.predict(features)
    return {"smurf_prediction": int(prediction[0])}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smurf Detection API. Use the /predict endpoint to make predictions."}