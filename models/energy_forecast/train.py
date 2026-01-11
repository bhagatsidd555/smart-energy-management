"""
Energy Demand Forecast Model Training (MVP-2)
--------------------------------------------
- Trains energy demand forecasting model
- Loads raw energy CSV from secured API (API key based)
- Automatically derives required features if not present
- No dependency on local CSV files
"""

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from ingestion.api_loader import load_csv_from_api


# =========================================================
# CONFIG
# =========================================================
MODEL_PATH = "models/energy_forecast/model.pkl"

ENERGY_API_URL = "YOUR_ENERGY_CSV_API_URL"
API_KEY = "YOUR_API_KEY"


# =========================================================
# FEATURE ENGINEERING & MAPPING
# =========================================================
def prepare_energy_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert raw energy CSV into model-ready features:
    - occupancy_density
    - traffic_score
    - weather_load
    - terminal_load_index
    """

    required_base_cols = [
        "passenger_count",
        "external_temp",
        "energy_kwh"
    ]

    for col in required_base_cols:
        if col not in df.columns:
            raise ValueError(f"❌ Required column '{col}' missing in energy CSV")

    # ---------- occupancy_density ----------
    # Assume max terminal capacity = 5000 passengers (configurable later)
    df["occupancy_density"] = df["passenger_count"] / 5000
    df["occupancy_density"] = df["occupancy_density"].clip(0, 1)

    # ---------- traffic_score ----------
    traffic_raw = df["passenger_count"]
    df["traffic_score"] = traffic_raw / traffic_raw.max()

    # ---------- weather_load ----------
    # Normalize external temperature impact
    df["weather_load"] = (df["external_temp"] - 20) / 15
    df["weather_load"] = df["weather_load"].clip(0, 1)

    # ---------- terminal_load_index ----------
    df["terminal_load_index"] = (
        0.4 * df["occupancy_density"] +
        0.3 * df["traffic_score"] +
        0.3 * df["weather_load"]
    )

    # ---------- target rename ----------
    df["energy_kw"] = df["energy_kwh"]

    return df


# =========================================================
# TRAINING PIPELINE
# =========================================================
def train_energy_model():
    print("🚀 Training Energy Demand Forecast Model (CSV API + Auto Mapping)")

    # 1️⃣ Load raw CSV data from API
    raw_df = load_csv_from_api(
        api_url=ENERGY_API_URL,
        api_key=API_KEY
    )

    # 2️⃣ Feature engineering & mapping
    df = prepare_energy_features(raw_df)

    # 3️⃣ Training data
    FEATURES = [
        "occupancy_density",
        "traffic_score",
        "weather_load",
        "terminal_load_index"
    ]

    X = df[FEATURES]
    y = df["energy_kw"]

    # 4️⃣ Model training
    model = RandomForestRegressor(
        n_estimators=150,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X, y)

    # 5️⃣ Save model
    joblib.dump(model, MODEL_PATH)

    print("✅ Energy forecast model trained successfully")
    print(f"📦 Model saved at: {MODEL_PATH}")
    print("📊 Training samples:", len(df))


# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    train_energy_model()
