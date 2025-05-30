import streamlit as st

# Each widget has an unique key/id automatically generated.
# If 2 widgets are same, they'll throw a StreamlitDuplicateElementId Error

st.button("Ok")
st.button("Ok",key="btn2") # NOW THEY DONT GIVE ANY ERRORS

# key = "btn2" refers to a unique identifier used 