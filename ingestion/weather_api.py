"""
Weather API Ingestion Module (MVP-2)

Responsibilities:
- Fetch real-time weather data
- Adjust HVAC and energy logic
"""

import random
from datetime import datetime


def fetch_weather_data() -> dict:
    """
    Simulated weather API response.
    Replace with OpenWeatherMap or similar API.
    """

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "outside_temperature": round(random.uniform(18.0, 38.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "weather_condition": random.choice(
            ["Clear", "Rain", "Cloudy", "Heatwave"]
        )
    }
