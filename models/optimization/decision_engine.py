"""
Decision Engine (MVP-2)

Combines:
- Real-time features
- ML predictions
- Safety constraints
- Automated control decision
"""

from constraints.safety_constraints import enforce_safety_constraints
from models.energy_forecast.predict import predict_energy_demand
from config.constants import (
    MAX_TEMPERATURE_C,
    MAX_CO2_PPM,
    BASELINE_ENERGY_KW
)


def generate_decision(features: dict) -> dict:
    """
    Generate automated energy control decision
    """

    safety = enforce_safety_constraints(features)

    if not safety["safe_to_proceed"]:
        return {
            "action": "MAINTAIN_CURRENT_SETTINGS",
            "reason": "Safety constraint violation",
            "safe": False
        }

    predicted_energy = predict_energy_demand(features)

    if features["co2"] > MAX_CO2_PPM:
        action = "INCREASE_VENTILATION"
        reason = "High CO₂ detected"

    elif predicted_energy > BASELINE_ENERGY_KW:
        action = "REDUCE_HVAC_LOAD"
        reason = "Predicted energy demand is high"

    else:
        action = "OPTIMIZE_INCREMENTALLY"
        reason = "Stable conditions"

    return {
        "action": action,
        "reason": reason,
        "safe": True,
        "predicted_energy_kw": predicted_energy
    }
