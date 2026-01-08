"""
Live Occupancy Prediction (MVP-2)
"""

import joblib

MODEL_PATH = "models/occupancy_prediction/model.pkl"

model = joblib.load(MODEL_PATH)


def predict_occupancy(arrivals: int, departures: int, traffic_score: float) -> int:
    """
    Predict near-future occupancy
    """

    X = [[arrivals, departures, traffic_score]]
    prediction = model.predict(X)[0]

    return max(int(prediction), 0)
