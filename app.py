import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="Weather vs Netflix Popularity", layout="wide")

st.title("🌦️ Weather vs 🎬 Netflix Popularity Dashboard")
st.write("Created by **Bhavana Shah** for Kiro Week 3 — The Data Weaver Challenge")

# -------------------------
# Inputs
# -------------------------
city = st.text_input("Enter a City", "Mumbai")

if st.button("Fetch Data"):
    # Get coordinates
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo = requests.get(geo_url).json()

    if "results" not in geo:
        st.error("City not found.")
    else:
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        # Weather API call
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
        weather = requests.get(weather_url).json()

        temp = weather["current"]["temperature_2m"]
        code = weather["current"]["weather_code"]

        st.subheader(f"🌡️ Current Weather in {city}")
        st.metric("Temperature (°C)", temp)

        # Netflix sample dataset
        df = pd.read_csv("data/sample_netflix.csv")

        st.subheader("🎬 Netflix Top 10 Popularity")
        st.dataframe(df)

        # Plot genre frequency
        fig = px.bar(df, x="genre", y="popularity", title="Genre Popularity")
        st.plotly_chart(fig)

        # Correlation (Dummy mapping for demonstration)
        df["temp"] = temp
        fig2 = px.scatter(df, x="temp", y="popularity", color="genre",
                          title="Temperature vs Netflix Genre Popularity")
        st.plotly_chart(fig2)
