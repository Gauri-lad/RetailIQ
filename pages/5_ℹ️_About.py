import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

from utils.ui import page_header

page_header(
    "📊 Sales Analysis",
    "Interactive analysis of retail sales performance."
)

st.markdown("""
## 📈 RetailIQ – AI-Powered Sales Forecasting & Demand Intelligence

RetailIQ is an end-to-end Business Intelligence dashboard developed using Python and Streamlit.

The project analyzes historical retail sales data, forecasts future sales using Machine Learning and Time Series models, detects unusual sales behaviour, and segments products according to demand.

The dashboard enables managers and decision-makers to monitor business performance and make data-driven decisions.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🎯 Objectives")

    st.markdown("""
- Analyze retail sales performance
- Forecast future sales
- Detect anomalies
- Segment products by demand
- Build an interactive BI dashboard
""")

with col2:

    st.subheader("🛠️ Technologies")

    st.markdown("""
- Python
- Pandas
- Plotly
- Streamlit
- Scikit-Learn
- XGBoost
- SARIMA
- Prophet
""")

st.divider()

st.subheader("📂 Dataset")

st.write("""
The project uses the Superstore Sales Dataset containing retail order information,
customer details, product categories, sales values, and shipping information.
""")

st.divider()

st.subheader("👩‍💻 Developer")

st.write("""
**Name:** Gauri Lad

**Program:** B.Tech – Artificial Intelligence & Data Science

**University:** Sanjivani University
""")

st.success("Thank you for exploring RetailIQ!")

st.divider()

st.caption(
    "RetailIQ • Built with Streamlit • © 2026 Gauri Lad"
)
