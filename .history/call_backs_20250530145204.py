import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1
    
if "info" not in st.session_state:
    st.session_state.info = {}