import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import calendar


#Gathering 2 data day and hour dashboard/data_siap.csvdashboard/data_siap.csv
df = pd.read_csv("/data_siap.csv")
day_df = pd.read_csv("data/data/day.csv")
hour_df = pd.read_csv("data/data/hour.csv")

# Navigation bar with "Beranda" (Home) and "Filter" options
selected_page = st.sidebar.selectbox(
    "Pilih Halaman (Select Page)",
    options=["Beranda (Home)", "Filter (Filter)"])

if selected_page == "Beranda (Home)":  
    # Judul dashboard
    st.title("Dashboard ")
    st.write("Data Penyewa sepeda")
    # Menampilkan DataFrame
    st.write("## Data hasil ")
    st.dataframe(df)

    # Statistik deskriptif
    st.write("## Statistik Deskriptif")
    st.write(df.describe())


#filter memunculkan fitur yang diinginkan
# Filter items dengan selectbox
elif selected_page == "Filter (Filter)":
    selected_filters = st.multiselect(
        "Pilih Filter",
        options=["temp", "atemp", "weathersit", "year"],
    )

    if "temp" in selected_filters:
        st.write("## Melihat Data Berdasarkan `temp`")
        st.write(df.groupby(by="temp").agg({
            "instant": "nunique",
            "cnt": ["max", "min", "mean", "std"]}))
        st.write("# Pengaruh Temp terhadap cnt (jumlah penyewa)")
        fig, ax = plt.subplots()
        temp_means = df.groupby('temp')['cnt'].mean()
        ax.bar(temp_means.index, temp_means.values)
        ax.set_xlabel("Temp")
        ax.set_ylabel("Rata-rata cnt")
        st.pyplot(fig)
        st.write("pada temperatur tinggi terdapat banyak penyewa, sedangka apabila temperatur rendah sedikit")
        # tampilkan histogram tiap bulannya
        plt.figure(figsize=(9,6))
        sns.boxplot(
            x="mnth",
            y="cnt",
            data=df,
            palette=["blue", "yellow", "purple", "pink", "red"]
        )

        plt.xlabel("Month")
        plt.ylabel("Total Rides")
        plt.title("Count by Year")
        plt.show()


    if "atemp" in selected_filters:
        st.write("## Melihat Data Berdasarkan `atemp`")
        st.write(df.groupby(by="atemp").agg({
            "instant": "nunique",
            "cnt": ["max", "min", "mean", "std"]}))
        st.write("# Pengaruh Atemp terhadap cnt (jumlah penyewa)")
        fig, ax = plt.subplots()
        atemp_means = df.groupby('atemp')['cnt'].mean()
        ax.bar(atemp_means.index, atemp_means.values)
        ax.set_xlabel("atemp")
        ax.set_ylabel("Rata-rata cnt")
        st.pyplot(fig)

    if "weathersit" in selected_filters:
        st.write("## Melihat Data Berdasarkan `weathersit`")
        st.write("1. Clear, Few clouds, Partly cloudy")
        st.write("2. Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
        st.write("3. Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
        st.write("4. Heavy Rain + Ice Pellets + Thunderstorm + Mist, Snow + Fog")
        st.write(df.groupby(by="weathersit").agg({
            "instant": "nunique",
            "cnt": ["max", "min", "mean", "std"]}))
        st.write("# Pengaruh Weathersit terhadap cnt(jumlah penyewa)")
        fig, ax = plt.subplots()
        weathersit_means = df.groupby('weathersit')['cnt'].mean()
        ax.bar(weathersit_means.index, weathersit_means.values)
        ax.set_xlabel("Weathersit")
        ax.set_ylabel("Rata-rata cnt")
        st.pyplot(fig)

    if "year" in selected_filters:
        st.write("## Melihat Data Berdasarkan `yr`")
        st.write(df.groupby(by="yr").agg({
            "instant": "nunique",
            "cnt": ["max", "min", "mean", "std"]}))
        st.write("# Pengaruh Tahun terhadap cnt (jumlah penyewa)")
        fig, ax = plt.subplots()
        year_means = df.groupby('yr')['cnt'].mean()
        ax.bar(year_means.index, year_means.values)
        ax.set_xlabel("Tahun")
        ax.set_ylabel("Rata-rata cnt")
        st.pyplot(fig)

#menampilkan data
df.describe()
df.head()

# tampilkan histogram tiap minggunya
plt.figure(figsize=(9,6))
sns.lineplot(
    x="weekday",
    y="cnt",
    data=df,
    palette=["navy","aqua", "yellow", "orange", "pink","magenta"]
)

plt.xlabel("weekday")
plt.ylabel("Total Rides")
plt.title("Count by weekday")
plt.show()
