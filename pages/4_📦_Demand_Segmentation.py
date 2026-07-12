import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Demand Segmentation", layout="wide")

from utils.ui import page_header

page_header(
    "📊 Sales Analysis",
    "Interactive analysis of retail sales performance."
)

segment = pd.read_csv("reports/segment_summary.csv")
sales = pd.read_csv("data/sales_data.csv")

product_sales = (
    sales.groupby("Product Name")["Sales"]
    .sum()
    .reset_index()
)

high = product_sales["Sales"].quantile(0.90)
medium = product_sales["Sales"].quantile(0.60)

def demand(x):
    if x >= high:
        return "High Demand"
    elif x >= medium:
        return "Medium Demand"
    else:
        return "Low Demand"

product_sales["Demand Segment"] = product_sales["Sales"].apply(demand)

st.markdown("---")

c1, c2, c3 = st.columns(3)

c1.metric(
    "High Demand Products",
    (product_sales["Demand Segment"]=="High Demand").sum()
)

c2.metric(
    "Medium Demand Products",
    (product_sales["Demand Segment"]=="Medium Demand").sum()
)

c3.metric(
    "Low Demand Products",
    (product_sales["Demand Segment"]=="Low Demand").sum()
)

st.markdown("---")

fig = px.pie(
    product_sales,
    names="Demand Segment",
    title="Demand Distribution",
    hole=0.45,
    color="Demand Segment"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("🏆 Top Selling Products")

top20 = (
    product_sales
    .sort_values("Sales", ascending=False)
    .head(20)
)

fig2 = px.bar(
    top20,
    x="Sales",
    y="Product Name",
    orientation="h",
    color="Sales"
)

fig2.update_layout(yaxis={"categoryorder":"total ascending"})

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

summary = (
    product_sales
    .groupby("Demand Segment")
    .agg(
        Products=("Product Name","count"),
        Average_Sales=("Sales","mean"),
        Total_Sales=("Sales","sum")
    )
    .reset_index()
)

st.dataframe(summary, use_container_width=True)

st.markdown("---")

st.subheader("🔍 Browse Products by Demand Segment")

selected = st.selectbox(
    "Choose a Demand Segment",
    ["High Demand", "Medium Demand", "Low Demand"]
)

filtered = product_sales[
    product_sales["Demand Segment"] == selected
]

st.dataframe(
    filtered.sort_values("Sales", ascending=False),
    use_container_width=True
)

st.markdown("---")

st.subheader("💡 Business Recommendations")

st.success("""
• High-demand products should receive priority inventory allocation.

• Medium-demand products can benefit from targeted marketing campaigns.

• Low-demand products should be reviewed for pricing, promotions, or discontinuation.

• Product segmentation helps optimize inventory management and maximize profitability.
""")

st.divider()

st.caption(
    "RetailIQ • Built with Streamlit • © 2026 Gauri Lad"
)
