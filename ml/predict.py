import joblib
import pandas as pd

model = joblib.load("ml/model.pkl")

def predict_risk(rainfall, traffic, distance):
    df = pd.DataFrame([{
        "rainfall": rainfall,
        "traffic": traffic,
        "distance_to_road": distance
    }])
    return float(model.predict(df)[0])
