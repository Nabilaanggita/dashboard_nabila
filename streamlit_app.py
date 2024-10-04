import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Required title for the menu
        options=["Home", "Projects", "Contact"],  # Options to display in the menu
    )
    if selected == "Home":
    st.title(f"You have selected {selected}")

    if selected == "Projects":
        st.title(f"You have selected {selected}")

    if selected == "Contact":
        st.title(f"You have selected {selected}")

#Gathering 2 data day and hour
day_df = pd.read_csv("data/data/day.csv")
hour_df = pd.read_csv("data/data/hour.csv")

new_order_df = pd.merge(
    left=day_df,
    right=hour_df,
    how="inner",
    left_on="instant",
    right_on="instant"
)
# Judul dashboard
st.title("Dashboard New Order")
st.write("Data New Order adalah data hour digabungkan dengan data day")
# Menampilkan DataFrame
st.write("## Data New Order")
st.dataframe(new_order_df)

# Statistik deskriptif
st.write("## Statistik Deskriptif")
st.write(new_order_df.describe())

#Buat filter memunculkan fitur yang diinginkan
# Filter items dengan selectbox
selected_filters = st.multiselect(
    "Pilih Filter",
    options=["temp", "atemp", "weathersit", "year"],
)

if "temp" in selected_filters:
    st.write("## Melihat Data Berdasarkan `temp_y`")
    st.write(new_order_df.groupby(by="temp_y").agg({
        "instant": "nunique",
        "cnt_y": ["max", "min", "mean", "std"]}))
    st.write("# Pengaruh Temp terhadap cnt (jumlah penyewa)")
    fig, ax = plt.subplots()
    temp_means = new_order_df.groupby('temp_y')['cnt_y'].mean()
    ax.bar(temp_means.index, temp_means.values)
    ax.set_xlabel("Temp")
    ax.set_ylabel("Rata-rata cnt")
    st.pyplot(fig)

if "atemp" in selected_filters:
    st.write("## Melihat Data Berdasarkan `atemp_y`")
    st.write(new_order_df.groupby(by="atemp_y").agg({
        "instant": "nunique",
        "cnt_y": ["max", "min", "mean", "std"]}))
    st.write("# Pengaruh Atemp terhadap cnt (jumlah penyewa)")
    fig, ax = plt.subplots()
    atemp_means = new_order_df.groupby('atemp_y')['cnt_y'].mean()
    ax.bar(atemp_means.index, atemp_means.values)
    ax.set_xlabel("atemp")
    ax.set_ylabel("Rata-rata cnt")
    st.pyplot(fig)

if "weathersit" in selected_filters:
    st.write("## Melihat Data Berdasarkan `weathersit_y`")
    st.write("1. Clear, Few clouds, Partly cloudy")
    st.write("2. Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
    st.write("3. Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
    st.write("4. Heavy Rain + Ice Pellets + Thunderstorm + Mist, Snow + Fog")
    st.write(new_order_df.groupby(by="weathersit_y").agg({
        "instant": "nunique",
        "cnt_y": ["max", "min", "mean", "std"]}))
    st.write("# Pengaruh Weathersit terhadap cnt(jumlah penyewa)")
    fig, ax = plt.subplots()
    weathersit_means = new_order_df.groupby('weathersit_y')['cnt_y'].mean()
    ax.bar(weathersit_means.index, weathersit_means.values)
    ax.set_xlabel("Weathersit")
    ax.set_ylabel("Rata-rata cnt")
    st.pyplot(fig)

if "year" in selected_filters:
    st.write("## Melihat Data Berdasarkan `yr_y`")
    st.write(new_order_df.groupby(by="yr_y").agg({
        "instant": "nunique",
        "cnt_y": ["max", "min", "mean", "std"]}))
    st.write("# Pengaruh Tahun terhadap cnt (jumlah penyewa)")
    fig, ax = plt.subplots()
    year_means = new_order_df.groupby('yr_y')['cnt_y'].mean()
    ax.bar(year_means.index, year_means.values)
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Rata-rata cnt")
    st.pyplot(fig)


