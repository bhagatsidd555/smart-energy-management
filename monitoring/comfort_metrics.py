"""
Comfort Metrics Module (MVP-2)

Responsibilities:
- Evaluate passenger comfort status
"""

from config.constants import (
    MIN_TEMPERATURE_C,
    MAX_TEMPERATURE_C
)


def evaluate_comfort_metrics(
    temperature: float,
    humidity: float
) -> dict:
    """
    Determine overall comfort status
    """

    if MIN_TEMPERATURE_C <= temperature <= MAX_TEMPERATURE_C:
        comfort = "COMPLIANT"
    else:
        comfort = "NON-COMPLIANT"

    return {
        "temperature": temperature,
        "humidity": humidity,
        "overall_comfort": comfort
    }
