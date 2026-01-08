"""
Live Monitoring Dashboard (MVP-2)

Responsibilities:
- Display real-time KPIs
- Show AI decisions & control status
- Display alerts
- Stream CSV data as live feed
"""

import streamlit as st
import time
import pandas as pd

from monitoring.energy_metrics import calculate_energy_metrics
from monitoring.comfort_metrics import evaluate_comfort_metrics
from monitoring.alerts import generate_alerts

from models.optimization.decision_engine import generate_decision
from control.simulation import execute_control


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Smart Energy Management System – MVP 2",
    layout="wide"
)

st.title("✈️ Smart Energy Management System")
st.caption("Real-time AI-driven Automated Control (CSV Live Simulation)")

AUTO_MODE = st.toggle("🔄 Enable Auto Control", value=True)

placeholder = st.empty()


# -------------------------------------------------
# LOAD CSV DATA (CACHED)
# -------------------------------------------------
@st.cache_data
def load_csv_data():
    return pd.read_csv("data/processed/energy_training.csv")


csv_data = load_csv_data()


# -------------------------------------------------
# FEATURE EXTRACTION FROM CSV
# -------------------------------------------------
def extract_features_from_row(row):
    return {
        "occupancy_density": row["occupancy_density"],
        "traffic_score": row["traffic_score"],
        "weather_load": row["weather_load"],
        "terminal_load_index": row["terminal_load_index"],
        "co2": int(400 + row["traffic_score"] * 800),
        "temperature": round(24 + row["weather_load"], 1),
        "humidity": 55   # ✅ REQUIRED by safety_constraints
    }




def extract_live_data_from_row(row):
    return {
        "occupancy": int(row["occupancy_density"] * 5000),
        "temperature": round(24 + row["weather_load"], 1),
        "humidity": 55,
        "energy_kw": round(row["energy_kw"], 2),
        "zone": "T1"
    }


# -------------------------------------------------
# DASHBOARD RENDER FUNCTION
# -------------------------------------------------
def display_dashboard(data: dict, features: dict):
    decision = generate_decision(features)

    with placeholder.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("👥 Occupancy", data["occupancy"])
        col2.metric("🌡️ Temperature (°C)", data["temperature"])
        st.divider()

        energy_kpi = calculate_energy_metrics(data["energy_kw"])
        comfort = evaluate_comfort_metrics(
            data["temperature"],
            data["humidity"]
        )

        col4, col5, col6 = st.columns(3)
        col4.metric("⚡ Energy (kW)", data["energy_kw"])
        col5.metric(
            "💰 Estimated Savings (%)",
            energy_kpi["estimated_savings_percent"]
        )
        col6.metric("🙂 Comfort Status", comfort["overall_comfort"])

        st.divider()

        st.subheader("🤖 AI Decision")
        st.info(f"{decision['action']} — {decision['reason']}")

        if AUTO_MODE:
            result = execute_control(decision, data["zone"])
            st.success(f"Control Status: {result['status']}")
        else:
            st.warning("Auto control disabled (Manual review mode)")

        alerts = generate_alerts(data)
        if alerts:
            st.subheader("🚨 Alerts")
            for alert in alerts:
                st.error(alert)


# -------------------------------------------------
# CSV → LIVE STREAM LOOP
# -------------------------------------------------
for _, row in csv_data.iterrows():
    live_data = extract_live_data_from_row(row)
    features = extract_features_from_row(row)

    display_dashboard(live_data, features)

    time.sleep(3)
