import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/sales_data.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True
    )

    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    return df