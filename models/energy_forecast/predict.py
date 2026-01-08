"""
Energy Demand Forecast Inference (MVP-2)
"""

import joblib

MODEL_PATH = "models/energy_forecast/model.pkl"

model = joblib.load(MODEL_PATH)


def predict_energy_demand(features: dict) -> float:
    """
    Predict energy demand (kW) for next interval
    """

    X = [[
        features["occupancy_density"],
        features["traffic_score"],
        features["weather_load"],
        features["terminal_load_index"]
    ]]

    prediction = model.predict(X)[0]
    return round(prediction, 2)
