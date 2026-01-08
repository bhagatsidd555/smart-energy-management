"""
Noise Filtering Module (MVP-2)

Responsibilities:
- Smooth noisy sensor readings
- Stabilize real-world IoT data
"""

from collections import deque

WINDOW_SIZE = 5


class MovingAverageFilter:
    def __init__(self):
        self.buffer = deque(maxlen=WINDOW_SIZE)

    def smooth(self, value: float) -> float:
        self.buffer.append(value)
        return round(sum(self.buffer) / len(self.buffer), 2)


temperature_filter = MovingAverageFilter()
humidity_filter = MovingAverageFilter()
co2_filter = MovingAverageFilter()
occupancy_filter = MovingAverageFilter()


def filter_iot_noise(data: dict) -> dict:
    data["temperature"] = temperature_filter.smooth(data["temperature"])
    data["humidity"] = humidity_filter.smooth(data["humidity"])
    data["co2"] = int(co2_filter.smooth(data["co2"]))
    data["occupancy"] = int(occupancy_filter.smooth(data["occupancy"]))
    return data
