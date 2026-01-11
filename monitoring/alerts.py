"""
Alerts Module – Smart Energy Management System (MVP-2)

Responsibilities:
- Generate real-time alerts from live inference data
- Handle missing keys safely
- Keep alert logic simple, explainable, and configurable
"""

from typing import Dict, List


# -------------------------------------------------
# DEFAULT THRESHOLDS (can be moved to config later)
# -------------------------------------------------
ENERGY_SPIKE_KW = 1200
TEMP_MIN = 22
TEMP_MAX = 26
HUMIDITY_MAX = 65
OCCUPANCY_MAX = 4000


def generate_alerts(data: Dict) -> List[str]:
    """
    Generate alerts based on live operational data.

    Expected data keys (safe if missing):
    - energy_kw
    - temperature
    - humidity
    - occupancy
    """

    alerts: List[str] = []

    # ---------------- Energy Alert ----------------
    energy_kw = data.get("energy_kw")
    if isinstance(energy_kw, (int, float)) and energy_kw > ENERGY_SPIKE_KW:
        alerts.append("⚡ High energy consumption detected")

    # ---------------- Temperature Alert ----------------
    temperature = data.get("temperature")
    if isinstance(temperature, (int, float)):
        if temperature < TEMP_MIN or temperature > TEMP_MAX:
            alerts.append("🌡️ Temperature out of comfort range")

    # ---------------- Humidity Alert ----------------
    humidity = data.get("humidity")
    if isinstance(humidity, (int, float)) and humidity > HUMIDITY_MAX:
        alerts.append("💧 High humidity level detected")

    # ---------------- Occupancy Alert ----------------
    occupancy = data.get("occupancy")
    if isinstance(occupancy, (int, float)) and occupancy > OCCUPANCY_MAX:
        alerts.append("👥 High crowd density detected")

    # ---------------- Fallback ----------------
    if not alerts:
        alerts.append("✅ All systems operating within normal limits")

    return alerts
