import streamlit as st
import pandas as pd
import joblib
from common import setup_page
setup_page()

st.title("Actual Data:", text_alignment='center')

df = pd.read_csv("data/clean/opensky_asia_features.csv")
df = df.sort_values("timestamp")
df = df.drop_duplicates(subset="icao24", keep="last")
color_map = {
    1: "#f7e305",
    0: "#e0d3d7",
    -1: "#d42424"
}
df['color'] = df['climb_phase'].map(color_map)

df = pd.DataFrame(
    {
        "latitude" : df['latitude'],
        'longitude': df['longitude'],
        'color': df['color']
    }
)

st.map(df, latitude="latitude", longitude='longitude', color='color')

st.markdown("""
<div style="margin-top:8px;">
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
    <div style="width:14px; height:14px; background:#f7e305;"></div>
    <span>Climb</span>
  </div>
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
    <div style="width:14px; height:14px; background:#d42424;"></div>
    <span>Descent</span>
  </div>
  <div style="display:flex; align-items:center; gap:8px;">
    <div style="width:14px; height:14px; background:#e0d3d7;"></div>
    <span>Level</span>
  </div>
</div>
""", unsafe_allow_html=True)
