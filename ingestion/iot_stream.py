"""
IoT Sensor Streaming Module (MVP-2)

Responsibilities:
- Consume real-time sensor data (MQTT-ready)
- Provide unified sensor payload for pipeline
- Can be replaced with real MQTT/Kafka consumers
"""

import time
import random
from datetime import datetime


def read_iot_sensors() -> dict:
    """
    Simulates real-time IoT sensor feed.
    Replace this logic with MQTT/Kafka consumer in production.
    """

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(21.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 75.0), 2),
        "co2": random.randint(400, 1300),
        "occupancy": random.randint(200, 1500),
        "zone": "Terminal-1"
    }


def stream_iot_data(poll_interval: int = 2):
    """
    Generator that continuously yields IoT sensor data
    """

    while True:
        yield read_iot_sensors()
        time.sleep(poll_interval)
