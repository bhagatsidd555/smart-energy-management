"""
Energy Demand Prediction – Inference Only
"""

import joblib
import pandas as pd
import os

MODEL_PATH = "models/energy_forecast/model.pkl"


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("❌ Energy model not found. Train model first.")
    return joblib.load(MODEL_PATH)


def predict_energy_demand(model, features: dict) -> float:
    """
    Predict energy demand safely from feature dict
    """

    REQUIRED_FEATURES = [
        "occupancy_density",
        "traffic_score",
        "weather_load",
        "terminal_load_index"
    ]

    input_df = pd.DataFrame([[features[f] for f in REQUIRED_FEATURES]],
                            columns=REQUIRED_FEATURES)

    prediction = model.predict(input_df)[0]
    return float(prediction)
