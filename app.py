import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Tech Mahindra Financial Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("company_financials_clean.csv")
comparison = pd.read_csv("comparison.csv")

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("📊 Financial Performance Dashboard: Tech Mahindra")

st.markdown("""
Welcome to the **Tech Mahindra Financial Dashboard**.

This dashboard provides an overview of the company's quarterly financial performance,
including Sales, Net Profit, Operating Profit Margin (OPM), and Machine Learning model comparison.
""")

st.divider()

# -------------------------------
# KPI Section
# -------------------------------
st.subheader("📌 Key Performance Indicators (Latest Quarter)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Latest Sales (₹ Cr)",
        f"{df['Sales'].iloc[-1]:,.0f}"
    )

with col2:
    st.metric(
        "Latest Net Profit (₹ Cr)",
        f"{df['Net profit'].iloc[-1]:,.0f}"
    )

with col3:
    st.metric(
        "Latest OPM (%)",
        f"{df['OPM'].iloc[-1]}%"
    )

st.divider()

# -------------------------------
# Financial Analytics
# -------------------------------
st.subheader("📈 Financial Analytics & Trends")

col1, col2 = st.columns(2)

# Sales & Net Profit
with col1:

    fig, ax = plt.subplots(figsize=(7,4))

    ax.plot(
        df["Period"],
        df["Sales"],
        marker="o",
        linewidth=2,
        label="Sales"
    )

    ax.plot(
        df["Period"],
        df["Net profit"],
        marker="o",
        linewidth=2,
        label="Net Profit"
    )

    ax.set_title("Sales & Net Profit Trend")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("₹ Crore")
    ax.legend()

    plt.xticks(rotation=45)

    st.pyplot(fig)

# OPM
with col2:

    fig, ax = plt.subplots(figsize=(7,4))

    ax.bar(
        df["Period"],
        df["OPM"]
    )

    ax.set_title("Operating Profit Margin (OPM)")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("OPM (%)")

    plt.xticks(rotation=45)

    st.pyplot(fig)

st.divider()

# -------------------------------
# Net Profit Analysis
# -------------------------------
st.subheader("📊 Net Profit Distribution")

fig, ax = plt.subplots(figsize=(8,4))

df.boxplot(
    column="Net profit",
    by="Profit_Trend",
    ax=ax
)

plt.suptitle("")
ax.set_title("Net Profit by Profit Trend")
ax.set_xlabel("Profit Trend")
ax.set_ylabel("Net Profit (₹ Cr)")

st.pyplot(fig)

st.divider()

# -------------------------------
# Model Comparison
# -------------------------------
st.subheader("🤖 Machine Learning Model Comparison")

with st.expander("Click to View Model Performance"):

    st.dataframe(
        comparison,
        use_container_width=True
    )

st.divider()

# -------------------------------
# Footer
# -------------------------------
st.caption("Developed by Khushboo | Tech Mahindra Financial Dashboard")
