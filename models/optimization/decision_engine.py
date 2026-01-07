"""
Decision Engine for Smart Energy Management System (MVP-1)

Responsibilities:
- Take live operational data (simulated)
- Enforce comfort & air-quality constraints
- Generate safe energy optimization recommendations
- Support human-in-the-loop approval
"""

from constraints.safety_constraints import enforce_safety_constraints
from config.constants import (
    LOW_OCCUPANCY_THRESHOLD,
    HIGH_OCCUPANCY_THRESHOLD,
    MAX_TEMPERATURE_C,
    MIN_TEMPERATURE_C,
    MAX_CO2_PPM,
    BASELINE_ENERGY_KW
)


def generate_recommendation(live_data: dict) -> dict:
    """
    Core MVP-1 optimization logic.

    Input:
        live_data = {
            "occupancy": int,
            "temperature": float,
            "humidity": float,
            "co2": int,
            "energy_kw": float
        }

    Output:
        recommendation dict
    """

    # -----------------------------
    # 1️⃣ Safety Gate (MANDATORY)
    # -----------------------------
    safety_result = enforce_safety_constraints(live_data)

    if not safety_result["safe_to_proceed"]:
        return {
            "action": "MAINTAIN_CURRENT_SETTINGS",
            "reason": "Safety constraint violation",
            "safe": False,
            "details": safety_result
        }

    # --------------------------------
    # 2️⃣ Optimization Decision Logic
    # --------------------------------
    occupancy = live_data["occupancy"]
    temperature = live_data["temperature"]
    co2 = live_data["co2"]
    current_energy = live_data["energy_kw"]

    # High comfort risk → prioritize passengers
    if temperature > MAX_TEMPERATURE_C or co2 > MAX_CO2_PPM:
        action = "INCREASE_COOLING_AND_VENTILATION"
        reason = "High temperature or CO₂ level detected"

    # Low traffic → energy saving
    elif occupancy < LOW_OCCUPANCY_THRESHOLD:
        action = "REDUCE_HVAC_LOAD"
        reason = "Low occupancy – energy optimization"

    # Peak traffic → maintain comfort
    elif occupancy > HIGH_OCCUPANCY_THRESHOLD:
        action = "MAINTAIN_CURRENT_SETTINGS"
        reason = "High occupancy – comfort priority"

    # Normal conditions
    else:
        action = "OPTIMIZE_INCREMENTALLY"
        reason = "Stable conditions – minor optimization"

    # --------------------------------
    # 3️⃣ Energy Impact Estimation
    # --------------------------------
    estimated_savings_percent = max(
        0,
        round(
            (BASELINE_ENERGY_KW - current_energy)
            / BASELINE_ENERGY_KW * 100,
            2
        )
    )

    # --------------------------------
    # 4️⃣ Final Recommendation Output
    # --------------------------------
    return {
        "action": action,
        "reason": reason,
        "safe": True,
        "estimated_energy_savings_percent": estimated_savings_percent,
        "inputs": live_data
    }
