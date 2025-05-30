import streamlit as st

st.title("Counter Example with Immediate Re-Run")

# Initialize 'count' in session state if it doesn't exist
if "count" not in st.session_state:
    st.session_state.count = 0

# Function to increment count and update immediately
def increment_and_rerun():
    st.session_state.count += 1

# Display current count
st.write(f"Current Count: {st.session_state.count}")

# Button that calls increment_and_rerun when clicked
st.button("Increment and Update Immediately", on_click=increment_and_rerun)
