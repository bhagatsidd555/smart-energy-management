"""
Data Collector Module (MVP-2)

Responsibilities:
- Collect operational data
- Store data for future retraining
"""

import csv
import os
from datetime import datetime

DATA_PATH = "data/processed/retraining_data.csv"

FIELDS = [
    "timestamp",
    "occupancy_density",
    "traffic_score",
    "weather_load",
    "terminal_load_index",
    "energy_kw",
    "temperature",
    "humidity"
]


def collect_data(features: dict, raw_data: dict):
    """
    Append live data to retraining dataset
    """

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    file_exists = os.path.isfile(DATA_PATH)

    with open(DATA_PATH, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.utcnow().isoformat(),
            "occupancy_density": features["occupancy_density"],
            "traffic_score": features["traffic_score"],
            "weather_load": features["weather_load"],
            "terminal_load_index": features["terminal_load_index"],
            "energy_kw": raw_data["energy_kw"],
            "temperature": raw_data["temperature"]
        })
