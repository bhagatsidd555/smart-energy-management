"""
Energy Feature Engineering (MVP-2)

Responsibilities:
- Compute terminal load index
"""

BASELINE_ENERGY_KW = 1500


def compute_terminal_load_index(
    energy_kw: float,
    occupancy_density: float,
    weather_load: float
) -> dict:
    """
    Load index = normalized energy demand
    """

    load_index = (
        (energy_kw / BASELINE_ENERGY_KW) *
        (1 + occupancy_density) *
        weather_load
    )

    return {
        "terminal_load_index": round(load_index, 2)
    }
