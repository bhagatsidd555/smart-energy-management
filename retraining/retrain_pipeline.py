"""
Retraining Pipeline (MVP-2)

Responsibilities:
- Trigger model retraining when drift is detected
"""

from retraining.model_evaluation import evaluate_model
from models.energy_forecast.train import train_energy_model


def retrain_models():
    """
    Retrain ML models using collected data
    """

    print("🔄 Retraining pipeline started")

    summary = evaluate_model()
    print("📊 Retraining Data Summary:", summary)

    # Retrain energy forecasting model
    train_energy_model(
        data_path="data/processed/retraining_data.csv"
    )

    print("✅ Retraining completed successfully")


if __name__ == "__main__":
    retrain_models()
