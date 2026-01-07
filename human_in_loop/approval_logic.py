"""
Approval Logic for Human-in-the-Loop – MVP 1

This module represents manual decision approval.
No automated execution is performed in MVP-1.
"""

from datetime import datetime

def approve_action(action: str, reason: str) -> dict:
    """
    Human approves AI recommendation.

    Returns approval metadata.
    """
    return {
        "decision": "APPROVED",
        "action": action,
        "reason": reason,
        "approved_by": "HUMAN_OPERATOR",
        "timestamp": datetime.now().isoformat()
    }


def reject_action(action: str, reason: str) -> dict:
    """
    Human rejects AI recommendation.

    Returns rejection metadata.
    """
    return {
        "decision": "REJECTED",
        "action": action,
        "reason": reason,
        "approved_by": "HUMAN_OPERATOR",
        "timestamp": datetime.now().isoformat()
    }
