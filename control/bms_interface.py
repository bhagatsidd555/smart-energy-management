"""
BMS Interface (MVP-2)

Responsibilities:
- Execute control actions on HVAC / ventilation / lighting
- Mock implementation (replace with real BMS APIs later)
"""

import logging

logging.basicConfig(
    filename="logs/control_actions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def execute_bms_action(action: str, zone: str):
    """
    Execute control action via BMS (mock)
    """

    message = f"BMS ACTION EXECUTED | Zone: {zone} | Action: {action}"
    print(message)
    logging.info(message)

    return {
        "status": "EXECUTED",
        "action": action,
        "zone": zone
    }
