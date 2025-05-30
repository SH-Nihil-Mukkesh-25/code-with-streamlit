import streamlit as st
from datetime import datetime

# Define limits
min_date = datetime(1900, 1, 1)
max_date = datetime.now()

# Initialize session state variables
if "name1" not in st.session_state:
    st.session_state.name1 = ""

if "birth_date" not in st.session_state:
    st.session_state.birth_date = None

if "age" not in st.session_state:
    st.session_state.age = None

st.title("Age Calculator")

# User input (OUTSIDE form for dynamic behavior)
st.session_state.name1 = st.text_input("Enter your first name", value=st.session_state.name1)

st.session_state.birth_date = st.date_input(
    "Enter your birth date", 
    min_value=min_date, 
    max_value=max_date, 
    value=st.session_state.birth_date if st.session_state.birth_date else min_date
)

# Dynamic age calculation
if st.session_state.birth_date:
    birth_date = st.session_state.birth_date
    age = max_date.year - birth_date.year
    if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
        age -= 1
    st.session_state.age = age
    st.write(f"Your calculated age is {age} years")

# Form just for submission (doesn’t handle input)
with st.form(key="user_info_form", clear_on_submit=False):
    submit_button1 = st.form_submit_button(label="Submit Form")

    if submit_button1:
        if not st.session_state.name1 or not st.session_state.birth_date:
            st.warning("Please fill in all form inputs")
        else:
            st.success(f"Thank you, {st.session_state.name1}. Your age is {st.session_state.age}.")
            st.balloons()
