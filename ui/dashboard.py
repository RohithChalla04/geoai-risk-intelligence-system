import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.title("GeoAI Risk Intelligence Dashboard")

# Fetch map data
map_data = requests.get("http://127.0.0.1:8000/map").json()

m = folium.Map(location=[28.2, -82.2], zoom_start=10)

for point in map_data:
    color = "green"
    if point["risk"] > 0.6:
        color = "red"
    elif point["risk"] > 0.3:
        color = "orange"

    folium.CircleMarker(
        location=[point["lat"], point["lon"]],
        radius=5,
        color=color,
        fill=True
    ).add_to(m)

st_folium(m, width=700)

st.subheader("🔍 Explain Risk")

rainfall = st.slider("Rainfall", 0, 100, 50)
traffic = st.slider("Traffic", 0, 100, 50)
distance = st.slider("Distance", 0, 10, 2)

if st.button("Explain"):
    res = requests.get(
        f"http://127.0.0.1:8000/explain?rainfall={rainfall}&traffic={traffic}&distance={distance}"
    ).json()

    st.write("Risk:", res["risk"])
    st.write(res["explanation"])
