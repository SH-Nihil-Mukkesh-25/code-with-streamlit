import streamlit as st
import time

# Cache this data for 60 seconds
@st.cache_data(ttl=60)
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3)  # Delay to mimic an API call
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)
