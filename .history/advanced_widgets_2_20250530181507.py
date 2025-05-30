import streamlit as st

if "checkbox" not in st.session_state:
    st.session_state.chekbox = False
    
def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field",value=st.session_state.checkbox,on_change=toggle_input)

if st.session_state