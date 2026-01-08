"""
Occupancy Feature Engineering (MVP-2)

Responsibilities:
- Compute occupancy density
- Support passenger heatmap generation
"""

TERMINAL_CAPACITY = {
    "T1": 5000,
    "T2": 7000
}


def compute_occupancy_density(data: dict) -> dict:
    """
    Density = occupancy / terminal capacity
    """

    zone = data.get("zone", "T1")
    capacity = TERMINAL_CAPACITY.get(zone, 5000)

    density = round(data["occupancy"] / capacity, 3)

    data["occupancy_density"] = min(density, 1.0)
    return data
