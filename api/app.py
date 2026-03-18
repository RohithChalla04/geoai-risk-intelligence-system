from fastapi import FastAPI
import geopandas as gpd
from ml.predict import predict_risk
from rag.geo_explainer import explain

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoAI API running"}

@app.get("/map")
def get_map():
    gdf = gpd.read_file("data/geo_data.geojson")

    results = []
    for _, row in gdf.iterrows():
        risk = predict_risk(row["rainfall"], row["traffic"], row["distance_to_road"])

        results.append({
            "lat": row.geometry.y,
            "lon": row.geometry.x,
            "risk": risk
        })

    return results

@app.get("/explain")
def get_explanation(rainfall: float, traffic: float, distance: float):
    risk = predict_risk(rainfall, traffic, distance)
    explanation = explain(rainfall, traffic, distance, risk)

    return {
        "risk": risk,
        "explanation": explanation
    }
