"""
Automated Control Simulation (MVP-2)

Responsibilities:
- Receive AI decisions
- Execute control actions
- Trigger fallback when unsafe
"""

from control.bms_interface import execute_bms_action
from control.fallback_controller import activate_fallback


def execute_control(decision: dict, zone: str) -> dict:
    """
    Execute AI decision safely
    """

    if not decision.get("safe", False):
        return activate_fallback(
            reason=decision.get("reason", "Unknown safety issue"),
            zone=zone
        )

    action = decision.get("action")

    if not action:
        return activate_fallback(
            reason="No valid action provided",
            zone=zone
        )

    return execute_bms_action(action=action, zone=zone)
