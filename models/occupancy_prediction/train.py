"""
Occupancy Prediction Model Training (MVP-2)
"""

import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression


MODEL_PATH = "models/occupancy_prediction/model.pkl"


def train_occupancy_model(data_path="data/processed/occupancy_training.csv"):
    df = pd.read_csv(data_path)

    FEATURES = [
        "arrivals",
        "departures",
        "traffic_score"
    ]

    X = df[FEATURES]
    y = df["occupancy"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Occupancy prediction model trained & saved")


if __name__ == "__main__":
    train_occupancy_model()
