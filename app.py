import streamlit as st
import pandas as pd
from logic import analyze

st.set_page_config(page_title="Healthcare Intelligence Dashboard", layout="wide")

st.title("🏥 Real-Time Healthcare Intelligence Dashboard")
st.caption("This system simulates real-time operational decision-making under resource constraints.")

# Load data
data = pd.read_csv("data.csv")

selected = st.selectbox("Select Hospital", data["hospital"])

row = data[data["hospital"] == selected].iloc[0]
st.subheader("🔧 Simulate Scenario")

extra_patients = st.slider(
    "Simulate incoming patients",
    0, 50,
    int(row["incoming_patients"])
)

row["incoming_patients"] = extra_patients
st.subheader("📊 Current Status")

col1, col2, col3 = st.columns(3)

col1.metric("Beds Available", row["beds_available"])
col2.metric("Critical Patients", row["critical_patients"])
col3.metric("Incoming Patients", row["incoming_patients"])

# Analyze
alerts, recommendations, score = analyze(row)

st.subheader("🚨 Alerts")
if alerts:
    for a in alerts:
        if "🚨" in a:
            st.error(a)
        else:
            st.warning(a)
else:
    st.success("No major alerts")

st.subheader("💡 Recommended Actions")
if recommendations:
    for r in recommendations:
        st.write("- " + r)
else:
    st.write("System stable")

st.subheader("📈 Decision Confidence Score")
st.progress(score / 100)
st.write(f"{score}% confidence in recommendations")

st.caption("Simulated system inspired by real-world decision platforms like Palantir")