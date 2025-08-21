from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from playerStats import *
    
model = joblib.load(r"C:\Users\Alec\Desktop\Projects\valmine\Analysis\model.pkl")

app = FastAPI()

class PredictRequest(BaseModel):
    match_id: str
    name: str
    tag: str


@app.post("/predict")
def predict(request: PredictRequest): 

    
    player_stats = get_player_stats(request.match_id, request.name, request.tag)
    player_stats_df = pd.DataFrame([player_stats])
    prediction = model.predict(player_stats_df)
    return {"smurf_prediction": int(prediction[0])}

