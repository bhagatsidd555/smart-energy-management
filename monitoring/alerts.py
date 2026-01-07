"""
Alerts – MVP 1
Generates alerts based on live conditions
"""

from config.constants import MAX_CO2_PPM, MAX_TEMPERATURE_C

def generate_alerts(live_data: dict) -> list:
    """
    Generate alert messages based on thresholds.
    """

    alerts = []

    if live_data["co2"] > MAX_CO2_PPM:
        alerts.append("⚠️ High CO₂ level detected – ventilation required")

    if live_data["temperature"] > MAX_TEMPERATURE_C:
        alerts.append("⚠️ Temperature exceeds comfort range")

    return alerts
