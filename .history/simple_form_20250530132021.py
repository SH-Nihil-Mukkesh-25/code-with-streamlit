import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_values = {
    "name" : None,
    "height" : None,
    "gender" : None,
    "dob" : None
}

min_date = datetime()

with st.form(key="user_input_form"):
    form_values["name"] = st.text_input("Enter Your Name : ")
    form_values["height"] = st.number_input("Enter Your Height (cm) : ")
    form_values["gender"] = st.selectbox("Gender" , ["Male" , "Female" , "Others"])
    form_values["dob"] = st.date_input("Enter Your DOB : ")

    
    submit_button = st.form_submit_button(label="Submit")
    
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please Fill All Fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key,value) in form_values.items():
                st.write(f"{key} : {value}")