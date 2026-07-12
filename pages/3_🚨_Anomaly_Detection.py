import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Anomaly Detection", layout="wide")

from utils.ui import page_header

page_header(
    "📊 Sales Analysis",
    "Interactive analysis of retail sales performance."
)

anomaly = pd.read_csv("reports/anomaly_report.csv")

anomaly["Order Date"] = pd.to_datetime(anomaly["Order Date"])

st.markdown("---")

col1, col2, col3 = st.columns(3)

total = len(anomaly)

iso = (anomaly["Isolation Forest"] == "Anomaly").sum()

z = (anomaly["Z-Score"] == "Anomaly").sum()

col1.metric("Total Weeks", total)
col2.metric("Isolation Forest Anomalies", iso)
col3.metric("Z-Score Anomalies", z)

st.markdown("---")
st.subheader("🔴 Isolation Forest Detection")

fig = px.line(
    anomaly,
    x="Order Date",
    y="Sales",
    title="Weekly Sales"
)

fig.add_scatter(
    x=anomaly[anomaly["Isolation Forest"]=="Anomaly"]["Order Date"],
    y=anomaly[anomaly["Isolation Forest"]=="Anomaly"]["Sales"],
    mode="markers",
    marker=dict(size=10, color="red"),
    name="Anomaly"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🟠 Z-Score Detection")

fig2 = px.line(
    anomaly,
    x="Order Date",
    y="Sales",
    title="Weekly Sales"
)

fig2.add_scatter(
    x=anomaly[anomaly["Z-Score"]=="Anomaly"]["Order Date"],
    y=anomaly[anomaly["Z-Score"]=="Anomaly"]["Sales"],
    mode="markers",
    marker=dict(size=10, color="orange"),
    name="Anomaly"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("📄 Detected Anomalies")

st.dataframe(
    anomaly[
        anomaly["Isolation Forest"]=="Anomaly"
    ],
    use_container_width=True
)
st.markdown("---")

st.subheader("💡 Business Insights")

st.info("""
• Sudden spikes may indicate successful promotions or festive sales.

• Extremely low sales could suggest stock shortages or operational issues.

• Monitoring anomalies helps improve inventory planning.

• Early anomaly detection enables faster business response.
""")

st.divider()

st.caption(
    "RetailIQ • Built with Streamlit • © 2026 Gauri Lad"
)