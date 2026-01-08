"""
Time Alignment Module (MVP-2)

Responsibilities:
- Normalize timestamps across sensor, energy, and API streams
"""

from datetime import datetime, timezone


def align_timestamp(data: dict) -> dict:
    try:
        data["timestamp"] = datetime.fromisoformat(
            data["timestamp"]
        ).astimezone(timezone.utc)
    except Exception:
        data["timestamp"] = datetime.now(timezone.utc)

    return data
