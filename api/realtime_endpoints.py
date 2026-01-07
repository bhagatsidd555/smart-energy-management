from fastapi import APIRouter
import random

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])

@router.get("/energy-kpis")
def energy_kpis():
    """
    Energy savings & efficiency KPIs
    """
    return {
        "current_consumption_kw": round(random.uniform(900, 1400), 2),
        "baseline_consumption_kw": 1500,
        "estimated_savings_percent": round(random.uniform(18, 30), 2)
    }


@router.get("/comfort-status")
def comfort_status():
    """
    Comfort & air-quality compliance
    """
    return {
        "temperature_ok": True,
        "humidity_ok": True,
        "co2_ok": True,
        "overall_status": "COMPLIANT"
    }


@router.get("/alerts")
def alerts():
    """
    Real-time alerts (MVP-1 simulated)
    """
    alerts = []

    if random.random() > 0.7:
        alerts.append("⚠️ High CO₂ detected in Zone B")

    if random.random() > 0.8:
        alerts.append("⚠️ Temperature deviation in Terminal 2")

    return {
        "alerts": alerts
    }
