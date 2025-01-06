import streamlit as st
import pandas as pd

st.title("Real-Time Health Advisory System")

def load_data():
    # Load the health data
    return pd.read_csv("health_data.csv", names=["timestamp", "heart_rate", "steps", "calories"])

# Button to load data
if st.button("Load Data"):
    data = load_data()
    st.write("Latest Health Data:")
    st.write(data.tail())
    st.line_chart(data[['heart_rate', 'steps', 'calories']])

    # Basic recommendation based on heart rate
    if data['heart_rate'].iloc[-1] > 100:
        st.warning("High heart rate detected! Recommendation: Take a rest and hydrate.")
    else:
        st.success("Heart rate is normal. Keep going!")
