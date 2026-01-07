"""
Comfort Metrics – MVP 1
Evaluates comfort compliance for monitoring
"""

from config.constants import (
    MIN_TEMPERATURE_C,
    MAX_TEMPERATURE_C,
    MIN_HUMIDITY_PERCENT,
    MAX_HUMIDITY_PERCENT
)

def evaluate_comfort_metrics(temperature: float, humidity: float) -> dict:
    """
    Evaluate comfort compliance.

    Returns:
        {
            "temperature_ok": bool,
            "humidity_ok": bool,
            "overall_comfort": str
        }
    """

    temperature_ok = MIN_TEMPERATURE_C <= temperature <= MAX_TEMPERATURE_C
    humidity_ok = MIN_HUMIDITY_PERCENT <= humidity <= MAX_HUMIDITY_PERCENT

    overall = "COMPLIANT" if temperature_ok and humidity_ok else "VIOLATION"

    return {
        "temperature_ok": temperature_ok,
        "humidity_ok": humidity_ok,
        "overall_comfort": overall
    }
