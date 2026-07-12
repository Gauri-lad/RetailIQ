import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

sales_df = load_data()

st.set_page_config(
    page_title="Sales Analysis",
    page_icon="📊",
    layout="wide"
)

from utils.ui import page_header

page_header(
    "📊 Sales Analysis",
    "Interactive analysis of retail sales performance."
)


st.divider()

col1, col2, col3 = st.columns(3)

# Year Filter
years = sorted(sales_df["Order Date"].dt.year.unique())

selected_year = col1.selectbox(
    "Select Year",
    options=["All"] + list(years)
)

# Region Filter
regions = sorted(sales_df["Region"].unique())

selected_region = col2.selectbox(
    "Select Region",
    options=["All"] + regions
)

# Category Filter
categories = sorted(sales_df["Category"].unique())

selected_category = col3.selectbox(
    "Select Category",
    options=["All"] + categories
)

filtered_df = sales_df.copy()

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.year == selected_year
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

    st.divider()

k1, k2, k3 = st.columns(3)

k1.metric(
    "💰 Total Sales",
    f"${filtered_df['Sales'].sum():,.0f}"
)

k2.metric(
    "📦 Orders",
    filtered_df["Order ID"].nunique()
)

k3.metric(
    "🛍 Products",
    filtered_df["Product Name"].nunique()
)

st.divider()

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales",
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🥧 Sales by Category")

    category_sales = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig_category = px.pie(
        category_sales,
        names="Category",
        values="Sales",
        hole=0.45
    )

    fig_category.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

with col2:

    st.subheader("📍 Sales by Region")

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        text="Sales",
        color="Sales",
        color_continuous_scale="Blues"
    )

    fig_region.update_traces(
        texttemplate="$%{y:,.0f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

    st.divider()

left, right = st.columns(2)
with left:

    st.subheader("🚚 Average Shipping Time")

    shipping = (
        filtered_df
        .groupby("Region")["Shipping Days"]
        .mean()
        .reset_index()
    )

    fig_ship = px.bar(
        shipping,
        x="Region",
        y="Shipping Days",
        color="Shipping Days",
        text_auto=".1f",
        color_continuous_scale="Teal"
    )

    fig_ship.update_layout(
        template="plotly_dark",
        coloraxis_showscale=False,
        height=450
    )

    st.plotly_chart(
        fig_ship,
        use_container_width=True
    )

with right:

    st.subheader("🏆 Top 10 Products")

    top_products = (
        filtered_df
        .groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    top_products.index += 1

    st.dataframe(
        top_products,
        use_container_width=True
    )

    st.divider()

st.caption(
    "RetailIQ • Built with Streamlit • © 2026 Gauri Lad"
)