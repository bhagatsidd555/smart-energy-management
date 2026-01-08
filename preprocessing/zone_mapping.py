"""
Zone Mapping Module

Responsibilities:
- Normalize zone names
- Map sensors to airport terminal zones
"""

ZONE_MAP = {
    "Terminal-1": "T1",
    "Terminal-2": "T2",
    "Domestic": "T1",
    "International": "T2"
}


def map_zone(data: dict) -> dict:
    raw_zone = data.get("zone", "UNKNOWN")
    data["zone"] = ZONE_MAP.get(raw_zone, raw_zone)
    return data
