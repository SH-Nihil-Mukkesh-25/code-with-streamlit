import streamlit as st

# Each widget has an unique key/id automatically generated.
# If 2 widgets are same, they'll throw a StreamlitDuplicateElementId Error

st.button("Ok")
st.button("Ok",key="")