import streamlit as st
from scipy.interpolate import RegularGridInterpolator
import numpy as np

# Define altitude and temperature grid
altitudes = [0, 2000, 4000, 6000, 8000, 10000]
temperatures = [-30, -20, -10, 0, 10, 20, 30, 40]

# Manifold pressure values (in. Hg)
filled_pressures = np.array([
    [21.5, 21.8, 22.1, 22.4, 22.6, 22.9, 23.1, 23.3],
    [20.9, 21.2, 21.5, 21.8, 22.1, 22.3, 22.5, 22.8],
    [20.4, 20.7, 21.0, 21.3, 21.5, 21.8, 22.0, 22.2],
    [19.9, 20.2, 20.5, 20.8, 21.0, 21.3, 21.5, 21.7],
    [19.5, 19.8, 20.1, 20.3, 20.6, 20.8, 21.0, 21.3],
    [19.1, 19.4, 19.6, 19.9, 19.9, 19.9, 19.9, 19.9]  # Filled missing with 19.9
])

# Set up interpolator
interp_func = RegularGridInterpolator(
    (altitudes, temperatures), filled_pressures, bounds_error=False, fill_value=None
)

# Streamlit UI
st.title("Manifold Pressure Calculator")
st.write("Estimate Maximum Continuous Manifold Pressure (in. Hg)")

alt_input = st.number_input("Pressure Altitude (ft)", min_value=0, max_value=12000, value=3500, step=100)
temp_input = st.number_input("Outside Air Temperature (°C)", min_value=-50, max_value=50, value=7, step=1)

if st.button("Calculate"):
    result = interp_func((alt_input, temp_input))
    st.success(f"Estimated Manifold Pressure: {result[0]:.2f} in. Hg")
