import streamlit as st

# SIDEBAR LAYOUT

st.sidebar.title("This is a Sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

# TABS LAYOUT

tab1,tab2,tab3 = st.tabs([]"Tab 1" , "Tab 2" , "Tab 3"])