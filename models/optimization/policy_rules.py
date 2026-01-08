"""
Policy Rules (MVP-2)

Combines business rules with ML predictions
"""

def apply_policy_constraints(decision: dict) -> dict:
    """
    Apply final policy checks
    """

    if not decision["safe"]:
        decision["final_action"] = "OVERRIDE_TO_SAFE_MODE"
    else:
        decision["final_action"] = decision["action"]

    return decision
