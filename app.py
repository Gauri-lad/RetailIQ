import streamlit as st

from utils.data_loader import load_data

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="RetailIQ",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Load Data
# ------------------------------
sales_df = load_data()

# ------------------------------
# Dashboard Title
# ------------------------------
st.title("📈 RetailIQ")

st.subheader("AI-Powered Sales Forecasting & Demand Intelligence")

st.markdown("""
Welcome to **RetailIQ**.

This dashboard presents a complete retail sales analytics solution built using
Machine Learning and Time Series Forecasting techniques.

Use the **sidebar** to navigate through the different sections of the dashboard.
""")

st.divider()

# ------------------------------
# KPI Cards
# ------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"${sales_df['Sales'].sum():,.0f}"
    )

with col2:
    st.metric(
        "📦 Orders",
        sales_df["Order ID"].nunique()
    )

with col3:
    st.metric(
        "🛍 Products",
        sales_df["Product Name"].nunique()
    )

with col4:
    st.metric(
        "🌍 Regions",
        sales_df["Region"].nunique()
    )

st.divider()

st.subheader("Project Workflow")

st.markdown("""
- 📊 Exploratory Data Analysis (EDA)
- 📈 Time Series Forecasting (SARIMA, Prophet, XGBoost)
- 🚨 Anomaly Detection
- 📦 Product Demand Segmentation
- 📉 Business Intelligence Dashboard
""")

st.divider()

st.caption(
    "RetailIQ • Built with Streamlit • © 2026 Gauri Lad"
)