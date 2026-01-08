"""
Flight Schedule Ingestion Module (MVP-2)

Responsibilities:
- Fetch live flight schedule data
- Provide passenger traffic signals
"""

import random
from datetime import datetime


def fetch_flight_schedule() -> dict:
    """
    Simulated flight schedule feed.
    Replace with real airport API integration.
    """

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "arrivals": random.randint(20, 80),
        "departures": random.randint(20, 80),
        "peak_traffic": random.choice([True, False]),
        "airport": "Demo International Airport"
    }
