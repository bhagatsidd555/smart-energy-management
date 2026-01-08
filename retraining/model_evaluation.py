"""
Model Evaluation Module (MVP-2)

Responsibilities:
- Detect data drift
- Evaluate model performance degradation
"""

import pandas as pd

ERROR_THRESHOLD_PERCENT = 15  # acceptable error


def detect_drift(
    actual_energy: float,
    predicted_energy: float
) -> bool:
    """
    Detect drift based on prediction error
    """

    error_percent = abs(
        actual_energy - predicted_energy
    ) / actual_energy * 100

    return error_percent > ERROR_THRESHOLD_PERCENT


def evaluate_model(data_path="data/processed/retraining_data.csv") -> dict:
    """
    Evaluate recent data quality
    """

    df = pd.read_csv(data_path)

    summary = {
        "records": len(df),
        "avg_energy": round(df["energy_kw"].mean(), 2),
        "avg_temperature": round(df["temperature"].mean(), 2)
    }

    return summary
