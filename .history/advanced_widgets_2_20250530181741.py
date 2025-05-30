import streamlit as st

# Initialize session state variables if they don't exist
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

# Checkbox with on_change callback
st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input, key="checkbox")

# Show input box only if checkbox is checked
if st.session_state.checkbox:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.user_input

st.write(f"User Input: {user_input}")
