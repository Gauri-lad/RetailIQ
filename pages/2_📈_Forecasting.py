import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Forecasting", layout="wide")

from utils.ui import page_header

page_header(
    "📊 Sales Analysis",
    "Interactive analysis of retail sales performance."
)



sarima = pd.read_csv("reports/sarima_predictions.csv")
prophet = pd.read_csv("reports/prophet_predictions.csv")
xgb = pd.read_csv("reports/xgboost_predictions.csv")
comparison = pd.read_csv("reports/model_comparison.csv")

# Load original sales data
sales_df = pd.read_csv("data/sales_data.csv")


# Convert dates
prophet["Date"] = pd.to_datetime(prophet["Date"])
sales_df["Order Date"] = pd.to_datetime(sales_df["Order Date"])

# Create monthly actual sales
monthly_sales = (
    sales_df
    .groupby(pd.Grouper(key="Order Date", freq="M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.columns = ["Date", "Actual"]

# Merge Actual values with Prophet predictions
prophet = prophet.merge(monthly_sales, on="Date", how="left")

# Reorder columns
prophet = prophet[["Date", "Actual", "Predicted"]]

st.write(prophet.head())

st.divider()

st.subheader("🏆 Model Performance Comparison")

st.dataframe(comparison, use_container_width=True)

best_model = comparison.loc[comparison["MAPE"].idxmin(), "Model"]

st.success(f"Best Performing Model : {best_model}")

st.markdown("---")
st.subheader("🏆 Best Forecasting Model")

best_model = comparison.loc[
    comparison["MAPE"].idxmin(),
    "Model"
]

best_mape = comparison["MAPE"].min()

st.success(
    f"""
### ✅ Best Performing Model: **{best_model}**

MAPE = **{best_mape:.3f}**

This model achieved the lowest forecasting error,
making it the most reliable for future retail sales prediction.
"""
)

st.divider()

st.header("📈 Forecast Visualizations")

tab1, tab2, tab3 = st.tabs([
    "SARIMA",
    "Prophet",
    "XGBoost"
])

with tab1:

    st.subheader("SARIMA Forecast")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=sarima["Date"],
        y=sarima["Actual"],
        mode="lines+markers",
        name="Actual"
    ))

    fig.add_trace(go.Scatter(
        x=sarima["Date"],
        y=sarima["Predicted"],
        mode="lines+markers",
        name="Predicted"
   ))

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

with tab2:

    st.subheader("Facebook Prophet Forecast")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=prophet["Date"],
        y=prophet["Actual"],
        mode="lines+markers",
        name="Actual"
    ))

    fig.add_trace(go.Scatter(
        x=prophet["Date"],
        y=prophet["Predicted"],
        mode="lines+markers",
        name="Predicted"
    ))

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

with tab3:

    st.subheader("XGBoost Forecast")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=xgb["Date"],
        y=xgb["Actual"],
        mode="lines+markers",
        name="Actual"
    ))

    fig.add_trace(go.Scatter(
        x=xgb["Date"],
        y=xgb["Predicted"],
        mode="lines+markers",
        name="Predicted"
    ))

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)


    st.write(prophet.head())

    st.markdown("---")

st.subheader("📋 Forecast Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Best Model",
    best_model
)

col2.metric(
    "Lowest MAPE",
    f"{best_mape:.3f}"
)

col3.metric(
    "Forecast Horizon",
    "3 Months"
)
st.markdown("---")

st.subheader("💡 Business Insights")

st.info("""
• XGBoost provides the highest forecasting accuracy.

• Sales are expected to remain stable over the forecast horizon.

• Inventory planning should prioritize high-demand months.

• Marketing campaigns can be scheduled during forecasted sales peaks.

• Business managers should continuously retrain the model using recent sales data.
""")

st.divider()

st.caption(
    "RetailIQ • Built with Streamlit • © 2026 Gauri Lad"
)