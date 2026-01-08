"""
Energy Meter Streaming Module (MVP-2)

Responsibilities:
- Stream real-time energy consumption data
- Integrate with smart meters in production
"""

import time
import random
from datetime import datetime


def read_energy_meter() -> dict:
    """
    Simulated smart energy meter reading
    """

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "energy_kw": round(random.uniform(800.0, 1800.0), 2),
        "zone": "Terminal-1"
    }


def stream_energy_data(poll_interval: int = 2):
    """
    Generator for real-time energy meter data
    """

    while True:
        yield read_energy_meter()
        time.sleep(poll_interval)
