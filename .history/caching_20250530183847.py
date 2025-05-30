import streamlit as st
import time

# cache_data is used for immutable data [ Use this when the data you return won’t change or be modified later ]
# Because caching only works well if the data stays the same after it's cached.

@st.cache_data(ttl=60) # Cache (Save) this data for 60 seconds # ttl = time to live 
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3)  # Delay to mimic an API call
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)

'''
If anyone asks for this data again within 60 seconds, 
just give them the already saved result instead of waiting 3 seconds again.
'''

'''
1. Dictionary is a mutable type, but when we return it from this cached function - We kind of make it immutable
2. If we modify this from outside , its not going to affect what's returned from the cache
'''


# We are going to have a ton of re-runs of our python script which is not efficient especially when we reach out to APIs
# Or we need to grab a data that might take a long time to complete

# If I already did something once and got the result,
# why not save it and just re-use it next time instead of doing it all over again?

# So in STREAMLIT, we can implement a Cache
# It will be hit for every single user across every single session to save us a significant amount of time.

# Streamlit operates as its own web server [ RENDERING OUR PYTHON CODE - AND MORE ]
