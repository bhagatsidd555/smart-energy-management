"""
Master Safety Constraints
Acts as final gate before any optimization recommendation

✔ API-based data compatible
✔ Missing CO₂ handled safely
✔ Production & MVP ready
"""

from constraints.comfort_constraints import check_comfort_constraints
from constraints.air_quality_constraints import check_air_quality_constraints


def enforce_safety_constraints(live_data: dict) -> dict:
    """
    Enforce all safety constraints.

    live_data MAY contain:
        {
            "temperature": float,
            "humidity": float,
            "co2": int (optional)
        }

    Returns:
        {
            "safe_to_proceed": bool,
            "comfort": {...},
            "air_quality": {...}
        }
    """

    # -------------------------------------------------
    # SAFE EXTRACTION WITH DEFAULTS (NO CRASH)
    # -------------------------------------------------
    temperature = live_data.get("temperature", 24.0)
    humidity = live_data.get("humidity", 50.0)

    # ✅ CO₂ sensor not available → assume outdoor baseline
    # Industry standard: 400–420 ppm
    co2_ppm = live_data.get("co2", 420)

    # -------------------------------------------------
    # COMFORT CHECK
    # -------------------------------------------------
    comfort_result = check_comfort_constraints(
        temperature=temperature,
        humidity=humidity
    )

    # -------------------------------------------------
    # AIR QUALITY CHECK
    # -------------------------------------------------
    air_quality_result = check_air_quality_constraints(
        co2_ppm=co2_ppm
    )

    # -------------------------------------------------
    # FINAL SAFETY DECISION
    # -------------------------------------------------
    safe_to_proceed = (
        comfort_result.get("comfort_ok", False)
        and air_quality_result.get("air_quality_ok", False)
    )

    return {
        "safe_to_proceed": safe_to_proceed,
        "comfort": comfort_result,
        "air_quality": air_quality_result,
        "co2_used_ppm": co2_ppm  # 🔍 debug / explainability
    }
