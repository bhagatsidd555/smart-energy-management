import os
import sys
import random
import time

import streamlit as st

# -------------------------------------------------
# Fix PYTHONPATH so internal modules work correctly
# -------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from models.optimization.decision_engine import generate_recommendation
from monitoring.energy_metrics import calculate_energy_metrics
from monitoring.comfort_metrics import evaluate_comfort_metrics
from monitoring.alerts import generate_alerts
from human_in_loop.approval_logic import approve_action, reject_action
from human_in_loop.audit_logger import log_decision

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart Energy Management ",
    layout="wide"
)

st.title("✈️ Smart Energy Management System – MVP 1")
st.caption("Real-time AI-driven Decision Support (Human-in-the-loop)")

# -----------------------------
# Session State Init (IMPORTANT)
# -----------------------------
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

# -----------------------------
# Simulated Live Data Generator
# -----------------------------
def get_live_data():
    return {
        "occupancy": random.randint(200, 1200),
        "temperature": round(random.uniform(22, 28), 1),
        "humidity": round(random.uniform(40, 70), 1),
        "co2": random.randint(450, 900),
        "energy_kw": round(random.uniform(800, 1500), 2),
    }

# -----------------------------
# Auto-refresh every 3 seconds
# (Streamlit-safe replacement for while True)
# -----------------------------
if time.time() - st.session_state.last_update > 3:
    st.session_state.last_update = time.time()
    st.rerun()

# -----------------------------
# Generate Live Snapshot
# -----------------------------
data = get_live_data()

recommendation = generate_recommendation(data)

energy_kpi = calculate_energy_metrics(data["energy_kw"])
comfort_status = evaluate_comfort_metrics(
    data["temperature"],
    data["humidity"]
)
alerts = generate_alerts(data)

# -----------------------------
# Dashboard Layout
# -----------------------------
col1, col2, col3 = st.columns(3)
col1.metric("👥 Occupancy", data["occupancy"])
col2.metric("🌡️ Temperature (°C)", data["temperature"])
col3.metric("🫁 CO₂ (ppm)", data["co2"])

st.divider()

col4, col5, col6 = st.columns(3)
col4.metric("⚡ Energy (kW)", data["energy_kw"])
col5.metric(
    "💰 Estimated Savings (%)",
    energy_kpi["estimated_savings_percent"]
)
col6.metric("🙂 Comfort Status", comfort_status["overall_comfort"])

st.divider()

st.subheader("🤖 AI Recommendation")
st.info(f"{recommendation['action']} — {recommendation['reason']}")

# -----------------------------
# Human-in-the-loop Actions
# -----------------------------
decision_key = f"{data['occupancy']}_{data['energy_kw']}"

colA, colB = st.columns(2)

if colA.button("✅ Approve", key=f"approve_{decision_key}"):
    decision = approve_action(
        recommendation["action"],
        recommendation["reason"]
    )
    log_decision(decision)
    st.success("Action Approved & Logged")

if colB.button("❌ Reject", key=f"reject_{decision_key}"):
    decision = reject_action(
        recommendation["action"],
        recommendation["reason"]
    )
    log_decision(decision)
    st.warning("Action Rejected & Logged")

# -----------------------------
# Alerts Section
# -----------------------------
if alerts:
    st.subheader("🚨 Alerts")
    for alert in alerts:
        st.error(alert)
