"""
Master Safety Constraints
Acts as final gate before any optimization recommendation
"""

from constraints.comfort_constraints import check_comfort_constraints
from constraints.air_quality_constraints import check_air_quality_constraints

def enforce_safety_constraints(live_data: dict) -> dict:
    """
    Enforce all safety constraints.

    live_data expects:
        {
            "temperature": float,
            "humidity": float,
            "co2": int
        }

    Returns:
        {
            "safe_to_proceed": bool,
            "comfort": {...},
            "air_quality": {...}
        }
    """

    comfort_result = check_comfort_constraints(
        temperature=live_data["temperature"],
        humidity=live_data["humidity"]
    )

    air_quality_result = check_air_quality_constraints(
        co2_ppm=live_data["co2"]
    )

    safe_to_proceed = (
        comfort_result["comfort_ok"]
        and air_quality_result["air_quality_ok"]
    )

    return {
        "safe_to_proceed": safe_to_proceed,
        "comfort": comfort_result,
        "air_quality": air_quality_result
    }
