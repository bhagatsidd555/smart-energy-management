from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter(prefix="/realtime", tags=["Realtime"])

@router.get("/metrics")
def get_live_metrics():
    """
    Simulated real-time ingestion:
    Flight + Weather + IoT + Energy meters
    """
    return {
        "timestamp": datetime.now(),
        "occupancy": random.randint(200, 1200),
        "temperature": round(random.uniform(22, 28), 1),
        "humidity": round(random.uniform(40, 70), 1),
        "co2": random.randint(450, 900),
        "energy_kw": round(random.uniform(800, 1500), 2),
    }


@router.get("/recommendation")
def get_ai_recommendation():
    """
    AI-driven optimization recommendation (MVP-1 logic)
    """
    occupancy = random.randint(200, 1200)
    temperature = random.uniform(22, 28)
    co2 = random.randint(450, 900)

    if temperature > 26 or co2 > 800:
        action = "Increase Cooling & Ventilation"
    elif occupancy < 400:
        action = "Reduce HVAC Load (Energy Saving)"
    else:
        action = "Maintain Current Settings"

    return {
        "timestamp": datetime.now(),
        "recommendation": action,
        "confidence": round(random.uniform(0.72, 0.95), 2)
    }
