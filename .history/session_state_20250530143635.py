import streamlit as st

# ************************************* WITHOUT SESSION STATE **************************************

# A simple counter variable, without session state
# counter = 0

# st.write(f"Counter value : {counter}")

# Button to increment the counter

# if st.button("Increment Counter"):
#     counter += 1
#     st.write(f"Counter incremented to {counter}")
# else:
#     st.write(f"Counter stays at {counter}")
    
# st.divider()

    
# ************************************* WITH SESSION STATE **************************************

# Session State is something that we can use to store values within the same user session.
# Each session is per user per run / per instance of the kind of web page.\

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter Incremented to {st.session_state.counter}")
    
if st.button("Reset"):
    st.session_state.counter = 0
    
else:
    st.write(f"Counter did not reset")
    
st.write(f"Counter value : ")