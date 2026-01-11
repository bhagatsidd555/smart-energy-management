"""
Main Entry Point – Smart Energy Management System (MVP-2)
"""

import os
import sys
from dotenv import load_dotenv

# FORCE load .env for Streamlit process
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

# -------------------------------------------------
# PROJECT PATH SETUP
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# -------------------------------------------------
# LOAD API CONFIG (DIRECT)
# -------------------------------------------------
from config.api_config import (
    ENERGY_API_URL,
    OCCUPANCY_API_URL,
    API_KEY
)

print("DEBUG ENERGY_API_URL =", ENERGY_API_URL)
print("DEBUG OCCUPANCY_API_URL =", OCCUPANCY_API_URL)
print("DEBUG API_KEY =", API_KEY)

# -------------------------------------------------
# SYSTEM INFO
# -------------------------------------------------
print("🚀 Starting Smart Energy Management System")
print("⚙️ Mode: Automated AI-driven Control (API + Pre-trained Models)")
print("🧠 Training: DISABLED (Inference Only)")
print("🔐 Data Source: Direct API Config")

# -------------------------------------------------
# LAUNCH STREAMLIT DASHBOARD
# -------------------------------------------------
import streamlit.web.cli as stcli

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        "monitoring/dashboards.py"
    ]
    sys.exit(stcli.main())
