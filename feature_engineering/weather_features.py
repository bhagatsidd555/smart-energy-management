"""
Weather Feature Engineering (MVP-2)

Responsibilities:
- Adjust HVAC demand based on outside weather
"""

def compute_weather_adjusted_load(
    outside_temperature: float,
    weather_condition: str
) -> float:
    """
    Returns load multiplier based on weather
    """

    load = 1.0

    if outside_temperature > 35:
        load += 0.3
    elif outside_temperature < 15:
        load += 0.2

    if weather_condition.lower() in ["heatwave"]:
        load += 0.2

    return round(load, 2)
