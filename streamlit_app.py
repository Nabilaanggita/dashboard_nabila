import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import calendar


#Gathering 2 data day and hour dashboard/data_siap.csvdashboard/data_siap.csv
df = pd.read_csv("data_siap.csv")

#mendefinisikan Semua fungsi yang akan dipakai

def count_by_day_df(df):
    day_df_count_2011 = df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return day_df_count_2011

def total_registered_df(day_df):
   reg_df =  day_df.groupby(by="dteday").agg({
      "registered": "sum"
    })
   reg_df = reg_df.reset_index()
   reg_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return reg_df

def total_casual_df(day_df):
   cas_df =  day_df.groupby(by="dteday").agg({
      "casual": ["sum"]
    })
   cas_df = cas_df.reset_index()
   cas_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return cas_df

datetime_columns = ["dteday"]
df.sort_values(by="dteday", inplace=True)
df.reset_index(inplace=True)   

for column in datetime_columns:
    df[column] = pd.to_datetime(df[column])

min_date_days = df["dteday"].min()
max_date_days = df["dteday"].max()




# Navigation bar with "Beranda" (Home) and "Filter" options
selected_page = st.sidebar.selectbox(
    "Pilih Halaman ",
    options=["Beranda", "tampilkan data"])

if selected_page == "Beranda":  
    # Judul dashboard
    st.title("Dashboard ")
    st.write("Data Penyewa sepeda")

    # Menampilkan DataFrame
    st.write("## Data hasil bersih ")
    st.dataframe(df)

    # Statistik deskriptif
    st.write("## Statistik Deskriptif")
    st.write(df.describe())


#filter memunculkan fitur yang diinginkan
# Filter items dengan selectbox
elif selected_page == "tampilkan data":
    selected_filters = st.multiselect(
        "Pilih Filter",
        options=["temp", "atemp", "weathersit", "year","weekday", "month", ])

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

        # tampilkan histogram tiap minggunyaif "weekday" in selected_filters:
    if "weekday" in selected_filters:
        st.write("## Melihat Data Berdasarkan `weekday`")
        st.write(df.groupby(by="yr").agg({
            "instant": "nunique",
            "cnt": ["max", "min", "mean", "std"]}))
        st.write("# Pengaruh weekday terhadap cnt (jumlah penyewa)")
        fig, ax = plt.subplots()
        year_means = df.groupby('weekday')['cnt'].mean()
        ax.bar(year_means.index, year_means.values)
        ax.set_xlabel("weekday")
        ax.set_ylabel("Rata-rata cnt")
        st.pyplot(fig) 

         # tampilkan histogram tiap bulannya
    if "month" in selected_filters:
        st.write("## Melihat Data Berdasarkan `mnth`")
        st.write(df.groupby(by="mnth").agg({
            "instant": "nunique",
            "cnt": ["max", "min", "mean", "std"]}))
        st.write("# Pengaruh Tahun terhadap cnt (jumlah penyewa)")
        fig, ax = plt.subplots()
        year_means = df.groupby('mnth')['cnt'].mean()
        ax.bar(year_means.index, year_means.values)
        ax.set_xlabel("month")
        ax.set_ylabel("Rata-rata cnt")
        st.pyplot(fig)
