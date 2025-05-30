import streamlit as st

st.title("User Information Form")

form_values = {
    "name" : None,
    "height" : None,
    "gender" : None,
    "dob" : None
}

with st.form(key="user_input_form"):
    form_values["name"] = st.text_input("Enter Your Name : ")
    form_values["height"] = st.number_input("Enter Your Height (cm) : ")
    form_values["gender"] = st.date_input("Enter Your DOB : ")
    form_values[D]
    
    submit_form = st.form_submit_button()