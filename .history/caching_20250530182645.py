import streamlit as st
import time

@st.cache_data(ttl=60) # Cache this data for 60 seconds
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3)  # Delay to mimic an API call
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)

# We are going to have a ton of re-runs of our python script which is not efficient especially when we reach out to APIs
# Or we need to grab a data that might take a long time to

# So in STREAMLIT, we can implement a Cache
# It will be hit for every single user across every single session to save us a significant amount of time.

# Streamlit operates as its own web server [ RENDERING OUR PYTHON CODE ]
