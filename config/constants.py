"""
Global constants for Smart Energy Management System
Used across constraints, optimization, monitoring
"""

# ------------------------
# Temperature Constraints
# ------------------------
MIN_TEMPERATURE_C = 22.0
MAX_TEMPERATURE_C = 26.0

# ------------------------
# Humidity Constraints
# ------------------------
MIN_HUMIDITY_PERCENT = 40
MAX_HUMIDITY_PERCENT = 70

# ------------------------
# Air Quality Constraints
# ------------------------
MAX_CO2_PPM = 800  # ppm (passenger comfort & safety)

# ------------------------
# Occupancy Thresholds
# ------------------------
LOW_OCCUPANCY_THRESHOLD = 400
HIGH_OCCUPANCY_THRESHOLD = 1000

# ------------------------
# Energy Constraints
# ------------------------
BASELINE_ENERGY_KW = 1500

# ------------------------
# Safety & Control
# ------------------------
MAX_ALLOWED_DEVIATION_PERCENT = 10
FAILSAFE_MODE = True

# ------------------------
# System Metadata
# ------------------------
SYSTEM_NAME = "Smart Energy Management MVP-1"
VERSION = "1.0"
