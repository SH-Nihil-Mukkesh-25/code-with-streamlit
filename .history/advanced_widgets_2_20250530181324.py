import streamlit as st

if "checkbox" not in st.session_state:
    st.session_state.chekbox = False
    
def toggle_input():
    st.session_state.checkbox = 