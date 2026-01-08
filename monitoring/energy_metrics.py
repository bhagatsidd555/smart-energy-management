"""
Energy Metrics Module (MVP-2)

Responsibilities:
- Calculate energy savings
- Track energy performance KPIs
"""

from config.constants import BASELINE_ENERGY_KW


def calculate_energy_metrics(current_energy_kw: float) -> dict:
    """
    Calculate energy savings percentage
    """

    savings = max(
        0,
        round(
            (BASELINE_ENERGY_KW - current_energy_kw)
            / BASELINE_ENERGY_KW * 100,
            2
        )
    )

    return {
        "current_energy_kw": current_energy_kw,
        "baseline_energy_kw": BASELINE_ENERGY_KW,
        "estimated_savings_percent": savings
    }
