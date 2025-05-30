import streamlit as st

st.title("User Information Form")

form_values = {
    "name" : None,
    "height" : None,
    "gender" : None,
    "dob" : None
}

with st.form(key="user_input_form"):
    name = st.text_input("Enter Your Name : ")
    height = st.number_input("Enter Your Height (cm) : ")
    
    submit_form = st.form_submit_button()