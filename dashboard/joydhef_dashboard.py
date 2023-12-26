
#            DASHBOARD joydhef Bike USING STREAMLIT       
# 
# Nama          : Krisna Hidayat                               
# Email         : krisnahidayat462@gmail.com                       
# Id Dicoding   : dicoding.com/users/krisna0703/academies            
# Github Pages  : krisna0703.github.io                      
# Created       : 19 Desember 2023                           

# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ==============================
# LOAD DATA
# ==============================
@st.cache_resource
def load_data():
    data = pd.read_csv("dataset/hour.csv")
    return data


data = load_data()


# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Joydhef Bike Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Krisna Hidayat**")
st.sidebar.markdown(
    "**• Email: [krisnahidayat462@gmail.com](krisnahidayat462@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [krisnahidayat](https://www.dicoding.com/users/krisna0703/)**")
st.sidebar.markdown(
    "**• LinkedIn: [Krisna Hidayat](https://www.linkedin.com/in/krisna-hidayat/)**")
st.sidebar.markdown(
    "**• Github: [krisnahidayat](https://github.com/krisna0703)**")


st.sidebar.title("Dataset Joydhef Bike")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())
# Show dataset source
st.sidebar.markdown("[Download Dataset](https://link-to-your-dataset)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')


# ==============================
# VISUALIZATION
# ==============================

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise joydhef bike count
    # st.subheader("Season-wise Joydhef Bike Count")

    # Mapping dari angka ke label musim
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Season-wise Joydhef Bike Count")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise joydhef bike count
    # st.subheader("Weather Situation-wise Joydhef Bike Count")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Weather Situation-wise Joydhef Bike Count")
    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)


# Hourly joydhef bike count
# st.subheader("Hourly Joydhef Bike Count")
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Joydhef Bike Count")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=400, width=600)

# Humidity vs. Joydhef Bike Count
# st.subheader("Humidity vs. Joydhef Bike Count")
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Joydhef Bike Count")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs. joydhef bike Count
# st.subheader("Wind Speed vs. Joydhef Bike Count")
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Joydhef Bike Count")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs. Joydhef Bike Count
# st.subheader("Temperature vs. Joydhef Bike Count")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Joydhef Bike Count")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)

# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Ini menampilkan visualisasi untuk sekumpulan data Joydhef Bike.")
