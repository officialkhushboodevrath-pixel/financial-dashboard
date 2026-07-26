import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("company_financials_clean.csv")
comparison = pd.read_csv("comparison.csv")


st.title("Financial Dashboard: Tech Mahindra")


# KPI cards
c1, c2, c3 = st.columns(3)

c1.metric("Sales", f"{df['Sales'].iloc[-1]:,.0f}")
c2.metric("Net Profit", f"{df['Net profit'].iloc[-1]:,.0f}")
c3.metric("OPM", f"{df['OPM'].iloc[-1]}%")


# Sales and Net Profit chart

st.subheader("Sales and Net Profit Trend")

fig, ax = plt.subplots()

ax.plot(df["Period"], df["Sales"], marker="o", label="Sales")
ax.plot(df["Period"], df["Net profit"], marker="o", label="Net Profit")

ax.legend()
plt.xticks(rotation=45)

st.pyplot(fig)



# OPM chart

st.subheader("OPM Percentage")

fig, ax = plt.subplots()

ax.bar(df["Period"], df["OPM"])

plt.xticks(rotation=45)

st.pyplot(fig)



# Net Profit box plot

st.subheader("Net Profit by Profit Trend")

fig, ax = plt.subplots()

df.boxplot(column="Net profit", by="Profit_Trend", ax=ax)

plt.suptitle("")

st.pyplot(fig)



# Model comparison

st.subheader("Model Comparison")

st.dataframe(comparison)
