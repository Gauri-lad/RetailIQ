import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/train.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce",
        format="mixed"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce",
        format="mixed"
    )

    df = df.dropna(subset=["Order Date"])

    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    return df