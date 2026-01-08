"""
Traffic Feature Engineering (MVP-2)

Responsibilities:
- Compute peak traffic score
"""

def compute_traffic_score(
    occupancy_density: float,
    arrivals: int,
    departures: int
) -> float:
    """
    Traffic score combines crowd density and flight activity
    """

    flight_load = (arrivals + departures) / 100
    traffic_score = round((occupancy_density * 0.6) + (flight_load * 0.4), 2)

    return min(traffic_score, 1.0)
