"""
Live Monitoring Dashboard (MVP-2)

Responsibilities:
- Load live data from secured CSV APIs
- Run inference using pre-trained models
- Display KPIs, AI decisions, alerts
- Auto-refresh safely (Streamlit-safe)
"""

# =================================================
# ABSOLUTE PROJECT ROOT FIX (CRITICAL)
# =================================================
import os
import sys
from dotenv import load_dotenv

CURRENT_FILE = os.path.abspath(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_FILE, "../../"))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Load .env explicitly (Streamlit does NOT auto-load)
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

print("✅ PROJECT ROOT:", PROJECT_ROOT)

# =================================================
# IMPORTS
# =================================================
import time
import streamlit as st
import pandas as pd

from ingestion.api_loader import load_csv_from_api
from models.energy_forecast.predict import load_model
from models.optimization.decision_engine import generate_decision
from monitoring.energy_metrics import calculate_energy_metrics
from monitoring.comfort_metrics import evaluate_comfort_metrics
from monitoring.alerts import generate_alerts

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(
    page_title="Smart Energy Management System – MVP 2",
    layout="wide"
)

st.title("✈️ Smart Energy Management System")
st.caption("Real-time AI-driven Automated Control (API Mode)")

# =================================================
# ENV CONFIG
# =================================================
ENERGY_API_URL = os.getenv("ENERGY_API_URL")
API_KEY = os.getenv("API_KEY")  # optional

if not ENERGY_API_URL:
    st.error("❌ ENERGY_API_URL not set in .env")
    st.stop()

# =================================================
# LOAD MODEL (CACHED)
# =================================================
@st.cache_resource
def load_energy_model():
    return load_model()

model = load_energy_model()

# =================================================
# LOAD API DATA (SHORT CACHE)
# =================================================
@st.cache_data(ttl=30)
def load_live_data():
    return load_csv_from_api(
        api_url=ENERGY_API_URL,
        api_key=API_KEY
    )

df = load_live_data()

if df is None or df.empty:
    st.warning("⚠️ No data received from API")
    st.stop()

# =================================================
# FEATURE ENGINEERING (ROBUST + SAFE)
# =================================================
def prepare_live_features(row: pd.Series) -> dict:
    passenger_count = int(row.get("passenger_count", 0))
    external_temp = float(row.get("external_temp", 30))
    internal_temp = float(row.get("internal_temp", 24))
    humidity = float(row.get("humidity", 50))
    energy_kwh = float(row.get("energy_kwh", 0))

    # Normalized features
    occupancy_density = min(passenger_count / 5000, 1.0)
    traffic_score = occupancy_density
    weather_load = min(max((external_temp - 20) / 15, 0), 1)

    terminal_load_index = (
        0.4 * occupancy_density +
        0.3 * traffic_score +
        0.3 * weather_load
    )

    # ✅ CO₂ estimation (sensor-less MVP)
    co2_ppm = int(420 + occupancy_density * 900)

    return {
        # --- ML features ---
        "occupancy_density": occupancy_density,
        "traffic_score": traffic_score,
        "weather_load": weather_load,
        "terminal_load_index": terminal_load_index,

        # --- Live metrics ---
        "energy_kw": energy_kwh,
        "temperature": internal_temp,
        "humidity": humidity,
        "occupancy": passenger_count,
        "co2": co2_ppm,
        "zone": row.get("terminal_area", "T1")
    }

# =================================================
# SESSION STATE (LIVE SIMULATION)
# =================================================
if "row_idx" not in st.session_state:
    st.session_state.row_idx = 0

row = df.iloc[st.session_state.row_idx]
data = prepare_live_features(row)

# =================================================
# AI PREDICTION (MODEL ONLY HERE)
# =================================================
features_df = pd.DataFrame([{
    "occupancy_density": data["occupancy_density"],
    "traffic_score": data["traffic_score"],
    "weather_load": data["weather_load"],
    "terminal_load_index": data["terminal_load_index"]
}])

predicted_energy = float(model.predict(features_df)[0])

# =================================================
# KPI CALCULATIONS
# =================================================
energy_kpi = calculate_energy_metrics(data["energy_kw"])
comfort = evaluate_comfort_metrics(
    data["temperature"],
    data["humidity"]
)

decision = generate_decision(data)
alerts = generate_alerts(data)

# =================================================
# DASHBOARD UI
# =================================================
col1, col2, col3 = st.columns(3)
col1.metric("👥 Occupancy", data["occupancy"])
col2.metric("🌡️ Temperature (°C)", round(data["temperature"], 1))
col3.metric("💧 Humidity (%)", round(data["humidity"], 1))

st.divider()

col4, col5, col6 = st.columns(3)
col4.metric("⚡ Energy (kW)", round(data["energy_kw"], 2))
col5.metric("🔮 Predicted Energy (kW)", round(predicted_energy, 2))
col6.metric("🙂 Comfort Status", comfort["overall_comfort"])

st.divider()

st.subheader("🤖 AI Decision")
st.info(f"{decision['action']} — {decision['reason']}")

st.subheader("🚨 Alerts")
if alerts:
    for alert in alerts:
        st.warning(alert)
else:
    st.success("✅ No alerts")

# =================================================
# AUTO REFRESH (STREAMLIT SAFE)
# =================================================
time.sleep(3)
st.session_state.row_idx = (st.session_state.row_idx + 1) % len(df)
st.rerun()
