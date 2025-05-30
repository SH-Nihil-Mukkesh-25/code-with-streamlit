import streamlit as st

# Initialize user_input in session_state if not present
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Checkbox to show/hide input field
show_input = st.checkbox("Show Input Field")

# Show input box only if checkbox is checked
if show_input:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input

# Display the current user input
st.write(f"User Input: {st.session_state.user_input}")
