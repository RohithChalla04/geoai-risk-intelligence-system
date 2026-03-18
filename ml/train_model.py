import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

np.random.seed(42)

data = pd.DataFrame({
    "rainfall": np.random.uniform(0, 100, 500),
    "traffic": np.random.uniform(0, 100, 500),
    "distance_to_road": np.random.uniform(0, 10, 500),
})

data["risk"] = (
    0.6 * data["rainfall"] +
    0.3 * data["traffic"] -
    0.2 * data["distance_to_road"]
) / 100

X = data[["rainfall", "traffic", "distance_to_road"]]
y = data["risk"]

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")
print("Model trained")
