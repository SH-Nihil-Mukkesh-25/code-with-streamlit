import streamlit as st

# ************************************* WITHOUT SESSION STATE **************************************

# A simple counter variable, without session state
counter = 0

st.write(f"Counter value : {counter}")

# Button to increment the counter

if st.button("Increment Counter"):
    counter += 1
    st.write(f"Counter incremented to {counter}")
else:
    st.write(f"Counter stays at {counter}")
    
# ************************************* WITH SESSION STATE **************************************

st.divider()

