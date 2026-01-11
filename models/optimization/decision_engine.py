"""
Decision Engine (MVP-2)

Purpose:
- Apply safety constraints
- Apply rule-based operational logic
- NO ML prediction here (handled in dashboard)
"""

from constraints.safety_constraints import enforce_safety_constraints


def generate_decision(live_data: dict) -> dict:
    """
    Generate control decision based on live data
    """

    # -------------------------------------------------
    # SAFETY GATE (MANDATORY)
    # -------------------------------------------------
    safety = enforce_safety_constraints(live_data)

    if not safety["safe_to_proceed"]:
        return {
            "action": "HOLD",
            "reason": "Safety constraints violated",
            "details": safety
        }

    # -------------------------------------------------
    # RULE-BASED LOGIC (MVP)
    # -------------------------------------------------
    occupancy = live_data.get("occupancy", 0)
    temperature = live_data.get("temperature", 24)

    if occupancy < 500:
        return {
            "action": "REDUCE_HVAC_LOAD",
            "reason": "Low occupancy detected"
        }

    if temperature > 26:
        return {
            "action": "INCREASE_COOLING",
            "reason": "High temperature detected"
        }

    return {
        "action": "MAINTAIN",
        "reason": "Conditions optimal"
    }
