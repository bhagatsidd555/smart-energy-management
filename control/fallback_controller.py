"""
Fallback Controller (MVP-2)

Responsibilities:
- Enforce safe fallback actions
- Triggered when safety constraints fail
"""

import logging

logging.basicConfig(
    filename="logs/system_events.log",
    level=logging.WARNING,
    format="%(asctime)s - %(message)s"
)


def activate_fallback(reason: str, zone: str):
    """
    Activate safe fallback mode
    """

    message = f"FALLBACK ACTIVATED | Zone: {zone} | Reason: {reason}"
    print(message)
    logging.warning(message)

    return {
        "status": "FALLBACK",
        "zone": zone,
        "reason": reason
    }
