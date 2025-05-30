import streamlit as st

st.title("User Information Form")

with st.form(key="user_input_form"):
    st.text_input("Enter Your Name : ")
    st.number_input("Enter Your Age : ")