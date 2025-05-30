import streamlit as st

st.write("Hello World")

# Any time something must be updated on the screen,Streamlit reruns your entire Script from TOP to BOTTOM

pressed = st.button("Press Me")
print(pressed)

# By default it is in 'false', when you press it becomes 'true'
# in Streamlit, pressing a button causes the entire script to rerun from the top.
# When a Streamlit 