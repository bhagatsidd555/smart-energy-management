"""
Occupancy Prediction Model Training (API-based – FINAL)
------------------------------------------------------
- JSON API वरून data load करतो
- arrivals, departures, traffic_score AUTO derive करतो
- CSV लागत नाही
- Production-ready training pipeline
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from ingestion.api_loader import load_csv_from_api


# =========================================================
# CONFIG
# =========================================================
MODEL_PATH = "models/occupancy_prediction/model.pkl"

OCCUPANCY_API_URL = "http://127.0.0.1:8000/api/get-merged-data"
API_KEY = None   # local API असल्यामुळे key लागत नाही


# =========================================================
# FEATURE ENGINEERING
# =========================================================
def prepare_occupancy_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert raw API JSON data into:
    arrivals, departures, traffic_score, occupancy
    """

    # ---------- Time column ----------
    if "timestamp" not in df.columns:
        raise ValueError("❌ 'timestamp' column missing")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["time_bucket"] = df["timestamp"].dt.floor("15min")

    # ---------- arrivals & departures ----------
    df["is_arrival"] = df["arrival_time"].notna().astype(int)
    df["is_departure"] = df["departure_time"].notna().astype(int)

    grouped = df.groupby("time_bucket").agg(
        arrivals=("is_arrival", "sum"),
        departures=("is_departure", "sum"),
        occupancy=("passenger_count", "sum")
    )

    # ---------- traffic score ----------
    traffic_raw = grouped["arrivals"] + grouped["departures"]
    grouped["traffic_score"] = (
        traffic_raw / traffic_raw.max()
        if traffic_raw.max() > 0 else 0
    )

    return grouped.reset_index(drop=True)


# =========================================================
# TRAINING PIPELINE
# =========================================================
def train_occupancy_model():
    print("🚀 Training Occupancy Prediction Model (API-based + Auto Mapping)")
    print(f"🌐 API URL: {OCCUPANCY_API_URL}")

    # 1️⃣ Load API data (JSON → DataFrame)
    raw_df = load_csv_from_api(
        api_url=OCCUPANCY_API_URL,
        api_key=API_KEY
    )

    if raw_df.empty:
        raise ValueError("❌ API returned empty dataset")

    # 2️⃣ Feature engineering
    df = prepare_occupancy_features(raw_df)

    # 3️⃣ Train model
    FEATURES = ["arrivals", "departures", "traffic_score"]
    X = df[FEATURES]
    y = df["occupancy"]

    model = LinearRegression()
    model.fit(X, y)

    # 4️⃣ Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("✅ Occupancy model trained successfully")
    print(f"📦 Model saved at: {MODEL_PATH}")
    print(f"📊 Training samples: {len(df)}")


# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    train_occupancy_model()
