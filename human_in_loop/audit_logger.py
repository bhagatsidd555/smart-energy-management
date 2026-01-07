"""
Audit Logger for Human-in-the-Loop – MVP 1

Stores all AI recommendations and human decisions
for traceability, compliance, and debugging.
"""

from datetime import datetime
import json
import os

LOG_FILE = "logs/decisions.log"


def log_decision(decision_payload: dict):
    """
    Persist decision payload to audit log.
    """

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "decision": decision_payload
    }

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
