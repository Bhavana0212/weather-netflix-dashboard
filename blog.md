# ✨ Weather vs Netflix Popularity — A Data Weaver Story

**By: Bhavana Shah**  
*AI for Bharat – Kiro Week 3 Challenge*

---

## 🚀 Introduction

Week 3 of the Kiro challenge pushed us to “weave” together two unrelated datasets to discover something meaningful.  
I chose to explore an unusual question:

> **Does the weather impact what people watch on Netflix?**

It turns out — there is a fascinating pattern.

---

## 🎯 Problem

People often talk about “rainy-day movies” or “summer binge watching,” but does data support this idea?  

The challenge required:

- Two unrelated data sources  
- A dashboard mash-up  
- Technical write-up  
- GitHub repo with `.kiro` folder  

---

## 💡 Solution

I built a **Streamlit dashboard** that combines:

1. **Real-time weather data** (Open-Meteo API)  
2. **Netflix Top-10 popularity dataset**

The dashboard allows users to:

- Enter any city  
- Fetch current weather  
- View Netflix’s top trending shows  
- Visualize genre popularity vs temperature  
- Explore correlations  

Example trends:

- 🌧 Rainy days → Higher Romance/Drama  
- 🔥 Hot days → Comedy & Action rise  

---

## 🧱 Architecture

User → Streamlit App → Weather API
→ Netflix Dataset (CSV)
→ Plotly Graphs → Dashboard UI

yaml
Copy code

---

## 🧪 How Kiro Helped

Kiro accelerated the project by:

- Generating API integration code  
- Creating dataset templates  
- Helping design the mash-up concept  
- Troubleshooting Streamlit errors  
- Speeding up documentation & blog creation  

I completed the entire dashboard **in hours instead of days** thanks to Kiro.

---

## 🧩 Key Code Snippet

```python
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
df = pd.read_csv("data/sample_netflix.csv")
fig = px.scatter(df, x="temp", y="popularity")
---
## 📊 Screenshots

### Dashboard Home
![Dashboard Home](screenshots/dashboard_home.png)

### Netflix Popularity Table
![Netflix Table](screenshots/netflix_table.png)

### Weather Metrics
![Weather Metrics](screenshots/weather_metrics.png)

### Scatter Plot
![Scatter Plot](screenshots/scatter_plot.png)


🔗 GitHub Repository

Weather vs Netflix Dashboard

🎉 Conclusion

This week’s challenge expanded my ability to combine APIs, visualizations, and storytelling.
The final dashboard not only completes the challenge but also reveals fun trends hidden in everyday data.
