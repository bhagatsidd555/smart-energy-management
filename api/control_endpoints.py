from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/control", tags=["Control"])

LOG_FILE = "logs/control_actions.log"

@router.post("/approve")
def approve_action(action: str):
    """
    Human approval endpoint (Phase-1 simulated control)
    """
    log = f"{datetime.now()} | APPROVED | {action}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return {
        "status": "approved",
        "action": action,
        "timestamp": datetime.now()
    }


@router.post("/reject")
def reject_action(action: str):
    """
    Human rejection endpoint
    """
    log = f"{datetime.now()} | REJECTED | {action}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return {
        "status": "rejected",
        "action": action,
        "timestamp": datetime.now()
    }
