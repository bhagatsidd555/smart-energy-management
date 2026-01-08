"""
Data Validation Module (MVP-2)

Responsibilities:
- Validate incoming real-time data
- Ensure required fields exist
- Prevent corrupted data from entering AI pipeline
"""

REQUIRED_IOT_FIELDS = [
    "timestamp",
    "temperature",
    "humidity",
    "occupancy",
    "zone"
]

REQUIRED_ENERGY_FIELDS = [
    "timestamp",
    "energy_kw",
    "zone"
]


def validate_iot_data(data: dict) -> dict:
    for field in REQUIRED_IOT_FIELDS:
        if field not in data:
            raise ValueError(f"Missing IoT field: {field}")

    if not (0 <= data["temperature"] <= 60):
        raise ValueError("Invalid temperature value")

    if not (0 <= data["humidity"] <= 100):
        raise ValueError("Invalid humidity value")

    if not (300 <= data["co2"] <= 5000):
        raise ValueError("Invalid CO₂ value")

    if data["occupancy"] < 0:
        raise ValueError("Invalid occupancy value")

    return data


def validate_energy_data(data: dict) -> dict:
    for field in REQUIRED_ENERGY_FIELDS:
        if field not in data:
            raise ValueError(f"Missing energy field: {field}")

    if data["energy_kw"] < 0:
        raise ValueError("Invalid energy reading")

    return data
