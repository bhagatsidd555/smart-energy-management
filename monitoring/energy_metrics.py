"""
Energy Metrics – MVP 1
Computes energy KPIs and estimated savings
"""

from config.constants import BASELINE_ENERGY_KW

def calculate_energy_metrics(current_energy_kw: float) -> dict:
    """
    Calculate energy KPIs.

    Returns:
        {
            "current_energy_kw": float,
            "baseline_energy_kw": float,
            "estimated_savings_percent": float
        }
    """

    savings_percent = max(
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
        "estimated_savings_percent": savings_percent
    }
