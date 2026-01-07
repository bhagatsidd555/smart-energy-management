"""
Comfort Constraints
Ensures passenger comfort by validating temperature and humidity ranges
"""

from config.constants import (
    MIN_TEMPERATURE_C,
    MAX_TEMPERATURE_C,
    MIN_HUMIDITY_PERCENT,
    MAX_HUMIDITY_PERCENT,
)

def check_comfort_constraints(temperature: float, humidity: float) -> dict:
    """
    Validate temperature and humidity against comfort thresholds.

    Returns:
        {
            "comfort_ok": bool,
            "violations": list[str]
        }
    """
    violations = []

    # Temperature checks
    if temperature < MIN_TEMPERATURE_C:
        violations.append(
            f"Temperature below comfort limit ({temperature}°C < {MIN_TEMPERATURE_C}°C)"
        )

    if temperature > MAX_TEMPERATURE_C:
        violations.append(
            f"Temperature above comfort limit ({temperature}°C > {MAX_TEMPERATURE_C}°C)"
        )

    # Humidity checks
    if humidity < MIN_HUMIDITY_PERCENT:
        violations.append(
            f"Humidity below comfort limit ({humidity}% < {MIN_HUMIDITY_PERCENT}%)"
        )

    if humidity > MAX_HUMIDITY_PERCENT:
        violations.append(
            f"Humidity above comfort limit ({humidity}% > {MAX_HUMIDITY_PERCENT}%)"
        )

    return {
        "comfort_ok": len(violations) == 0,
        "violations": violations
    }
