"""
Energy Demand Forecast Model Training (MVP-2)

Predicts future energy demand based on operational features
"""

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor


MODEL_PATH = "models/energy_forecast/model.pkl"


def train_energy_model(data_path="data/processed/energy_training.csv"):
    df = pd.read_csv(data_path)

    FEATURES = [
        "occupancy_density",
        "traffic_score",
        "weather_load",
        "terminal_load_index"
    ]

    X = df[FEATURES]
    y = df["energy_kw"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Energy forecast model trained & saved")


if __name__ == "__main__":
    train_energy_model()
