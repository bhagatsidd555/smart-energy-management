"""
Air Quality Constraints
Ensures indoor air quality remains within safe CO₂ limits
"""

from config.constants import MAX_CO2_PPM

def check_air_quality_constraints(co2_ppm: int) -> dict:
    """
    Validate CO₂ level.

    Returns:
        {
            "air_quality_ok": bool,
            "violation": str | None
        }
    """
    if co2_ppm > MAX_CO2_PPM:
        return {
            "air_quality_ok": False,
            "violation": f"CO₂ level too high ({co2_ppm} ppm > {MAX_CO2_PPM} ppm)"
        }

    return {
        "air_quality_ok": True,
        "violation": None
    }
