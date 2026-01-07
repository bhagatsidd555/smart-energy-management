"""
Main entry point for Smart Energy Management System – MVP 1

MVP-1 Scope:
- Launch Streamlit dashboard
- No real-time Kafka / MQTT
- No BMS automation
- Human-in-the-loop decision support only
"""

import os
import sys

# Ensure project root is in PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


def run_dashboard():
    """
    Starts the MVP-1 Streamlit dashboard
    """
    dashboard_path = os.path.join(
        PROJECT_ROOT,
        "monitoring",
        "dashboards.py"
    )

    if not os.path.exists(dashboard_path):
        raise FileNotFoundError("dashboards.py not found in monitoring/")

    os.system(f"streamlit run {dashboard_path}")


if __name__ == "__main__":
    print("🚀 Starting Smart Energy Management System – MVP 1")
    print("📊 Mode: Human-in-the-loop Decision Support")
    print("⚠️ Automation & BMS control: DISABLED (MVP-2)")
    run_dashboard()
