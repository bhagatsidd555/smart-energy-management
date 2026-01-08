import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)

print("🚀 Starting Smart Energy Management System")
print("⚙️ Mode: Automated AI-driven Control (Simulation)")
print("⚠️ Deployment: DISABLED")

import streamlit.web.cli as stcli

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        "monitoring/dashboards.py"
    ]
    sys.exit(stcli.main())
