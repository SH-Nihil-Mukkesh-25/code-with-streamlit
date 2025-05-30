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
    form_values["gender"] = st.selectbox("Gender" , ["Male" , "Female" , "Others"])
    form_values["dob"] = st.date_input("Enter Your DOB : ")

    
    submit_button = st.form_submit_button()
    
    if submit_button:
        if not all 